"""Train two-stage CatBoost models without shop_id; block is optional at prediction time."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
from catboost import CatBoostRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"
CAT_FEATURES = ["state", "district", "block", "commodity"]
BASE_FEATURES = [
    "state", "district", "block", "commodity", "year", "month_number",
    "opening_stock_kg", "received_stock_kg", "beneficiaries", "transactions",
    "storage_capacity_kg", "storage_days", "delivery_delay_days", "previous_wastage_kg",
]
STAGE1_TARGET, STAGE2_TARGET = "distributed_stock_kg", "wastage_kg"
REQUIRED_COLUMNS = set([c for c in BASE_FEATURES if c not in {"year", "month_number", "block"}] + [STAGE1_TARGET, STAGE2_TARGET, "month"])

def prepare_data(path: Path) -> pd.DataFrame:
    data = pd.read_csv(path)
    missing = sorted(REQUIRED_COLUMNS - set(data.columns))
    if missing: raise ValueError(f"Dataset is missing required columns: {missing}")
    data["month"] = pd.to_datetime(data["month"], format="%Y-%m", errors="coerce")
    if data["month"].isna().any(): raise ValueError("Some month values could not be parsed as YYYY-MM.")
    data["year"], data["month_number"] = data["month"].dt.year.astype(int), data["month"].dt.month.astype(int)
    for col in CAT_FEATURES:
        if col not in data.columns: data[col] = "UNKNOWN"
        data[col] = data[col].fillna("UNKNOWN").astype(str).replace("", "UNKNOWN")
    if data[list(REQUIRED_COLUMNS)].isna().any().any(): raise ValueError("Required model columns contain missing values.")
    return data.sort_values("month").reset_index(drop=True)

def make_model(iterations: int = 600) -> CatBoostRegressor:
    return CatBoostRegressor(loss_function="RMSE", eval_metric="RMSE", iterations=iterations,
        depth=8, learning_rate=0.05, random_seed=42, verbose=False,
        allow_writing_files=False, thread_count=-1)

def metric_pack(actual, predicted):
    return {"mae": round(float(mean_absolute_error(actual, predicted)), 4),
            "rmse": round(float(np.sqrt(mean_squared_error(actual, predicted))), 4),
            "r2": round(float(r2_score(actual, predicted)), 5)}

def chronological_oof_predictions(train: pd.DataFrame, iterations: int) -> pd.Series:
    unique_months = np.array(sorted(train["month"].unique()))
    if len(unique_months) < 8: raise ValueError("At least 8 distinct months are needed for OOF training.")
    oof = pd.Series(np.nan, index=train.index, dtype=float)
    for fold, (fit_idx, pred_idx) in enumerate(TimeSeriesSplit(n_splits=4).split(unique_months), 1):
        fit_months, pred_months = unique_months[fit_idx], unique_months[pred_idx]
        fit_rows, pred_rows = train[train.month.isin(fit_months)], train[train.month.isin(pred_months)]
        model = make_model(iterations)
        model.fit(fit_rows[BASE_FEATURES], fit_rows[STAGE1_TARGET], cat_features=CAT_FEATURES)
        oof.loc[pred_rows.index] = model.predict(pred_rows[BASE_FEATURES])
        print(f"OOF fold {fold}: {len(fit_rows):,} fit rows, {len(pred_rows):,} predicted rows")
    return oof

def train(data_path: Path, holdout_months: int = 4, iterations: int = 600) -> dict:
    data = prepare_data(data_path)
    months = np.array(sorted(data.month.unique()))
    if len(months) <= holdout_months + 5: raise ValueError("Not enough distinct months for requested holdout.")
    test_months = months[-holdout_months:]
    train_data, test_data = data[~data.month.isin(test_months)].copy(), data[data.month.isin(test_months)].copy()

    stage1 = make_model(iterations)
    stage1.fit(train_data[BASE_FEATURES], train_data[STAGE1_TARGET], cat_features=CAT_FEATURES)
    p1 = stage1.predict(test_data[BASE_FEATURES])

    oof = chronological_oof_predictions(train_data, iterations)
    stage2_train = train_data.loc[oof.notna()].copy()
    stage2_train["stage1_predicted_distribution_kg"] = oof.loc[oof.notna()]
    stage2_features = BASE_FEATURES + ["stage1_predicted_distribution_kg"]
    stage2 = make_model(iterations)
    stage2.fit(stage2_train[stage2_features], stage2_train[STAGE2_TARGET], cat_features=CAT_FEATURES)
    test_features = test_data[BASE_FEATURES].copy()
    test_features["stage1_predicted_distribution_kg"] = p1
    p2 = stage2.predict(test_features[stage2_features])

    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    stage1.save_model(str(MODEL_DIR / "stage1_distribution.cbm"))
    stage2.save_model(str(MODEL_DIR / "stage2_wastage.cbm"))
    results = {
        "dataset_rows": int(len(data)), "train_rows": int(len(train_data)),
        "stage2_oof_train_rows": int(oof.notna().sum()), "test_rows": int(len(test_data)),
        "train_period": [train_data.month.min().strftime("%Y-%m"), train_data.month.max().strftime("%Y-%m")],
        "test_period": [test_data.month.min().strftime("%Y-%m"), test_data.month.max().strftime("%Y-%m")],
        "stage1_distribution": metric_pack(test_data[STAGE1_TARGET], p1),
        "stage2_wastage": metric_pack(test_data[STAGE2_TARGET], p2),
        "base_features": BASE_FEATURES, "categorical_features": CAT_FEATURES,
        "stage2_features": stage2_features,
        "note": "Chronological holdout; Stage 2 uses expanding-window OOF Stage-1 predictions. shop_id excluded. block is optional and defaults to UNKNOWN when absent. Leakage fields (actual closing stock, wastage, wastage percentage, risk level, damaged stock) excluded."
    }
    (MODEL_DIR / "metrics.json").write_text(json.dumps(results, indent=2))
    print(json.dumps(results, indent=2))
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=ROOT / "data/raw/Datasetfood.csv")
    parser.add_argument("--holdout-months", type=int, default=4)
    parser.add_argument("--iterations", type=int, default=600)
    args = parser.parse_args()
    train(args.data, args.holdout_months, args.iterations)
