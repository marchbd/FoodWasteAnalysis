"""Train the two-stage food distribution and wastage models.

Run from the repository root:
    python -m training.train_models --data data/raw/Datasetfood.csv

The last N months are held out as a chronological test set. Stage 2 is trained
on expanding-window out-of-fold predictions from Stage 1 to reduce
training/serving mismatch.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from catboost import CatBoostRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import TimeSeriesSplit

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"

CAT_FEATURES = ["shop_id", "state", "district", "block", "commodity"]
BASE_FEATURES = [
    "shop_id", "state", "district", "block", "commodity",
    "year", "month_number",
    "opening_stock_kg", "received_stock_kg",
    "beneficiaries", "transactions",
    "storage_capacity_kg", "storage_days",
    "delivery_delay_days", "previous_wastage_kg",
]
STAGE1_TARGET = "distributed_stock_kg"
STAGE2_TARGET = "wastage_kg"
REQUIRED_COLUMNS = set(BASE_FEATURES + [STAGE1_TARGET, STAGE2_TARGET, "month"])


def prepare_data(path: Path) -> pd.DataFrame:
    data = pd.read_csv(path)
    missing = sorted(REQUIRED_COLUMNS - set(data.columns))
    if missing:
        raise ValueError(f"Dataset is missing required columns: {missing}")

    data["month"] = pd.to_datetime(data["month"], format="%Y-%m", errors="coerce")
    if data["month"].isna().any():
        raise ValueError("Some month values could not be parsed as YYYY-MM.")

    data["year"] = data["month"].dt.year.astype(int)
    data["month_number"] = data["month"].dt.month.astype(int)
    data = data.sort_values("month").reset_index(drop=True)

    if data[list(REQUIRED_COLUMNS)].isna().any().any():
        raise ValueError("Required model columns contain missing values.")
    return data


def make_model(iterations: int = 600) -> CatBoostRegressor:
    return CatBoostRegressor(
        loss_function="RMSE",
        eval_metric="RMSE",
        iterations=iterations,
        depth=8,
        learning_rate=0.05,
        random_seed=42,
        verbose=False,
        allow_writing_files=False,
        thread_count=-1,
    )


def metric_pack(actual: pd.Series, predicted: np.ndarray) -> dict[str, float]:
    return {
        "mae": round(float(mean_absolute_error(actual, predicted)), 4),
        "rmse": round(float(np.sqrt(mean_squared_error(actual, predicted))), 4),
        "r2": round(float(r2_score(actual, predicted)), 5),
    }


def chronological_oof_predictions(
    train: pd.DataFrame, iterations: int
) -> pd.Series:
    """Return Stage-1 predictions for rows predicted by a model trained only
    on earlier months. Rows in the initial warm-up window remain NaN.
    """
    unique_months = np.array(sorted(train["month"].unique()))
    if len(unique_months) < 8:
        raise ValueError("At least 8 distinct months are needed for OOF training.")

    splitter = TimeSeriesSplit(n_splits=4)
    oof = pd.Series(np.nan, index=train.index, dtype=float)

    for fold, (fit_month_idx, predict_month_idx) in enumerate(splitter.split(unique_months), 1):
        fit_months = unique_months[fit_month_idx]
        predict_months = unique_months[predict_month_idx]
        fit_rows = train[train["month"].isin(fit_months)]
        predict_rows = train[train["month"].isin(predict_months)]

        model = make_model(iterations)
        model.fit(
            fit_rows[BASE_FEATURES],
            fit_rows[STAGE1_TARGET],
            cat_features=CAT_FEATURES,
        )
        oof.loc[predict_rows.index] = model.predict(predict_rows[BASE_FEATURES])
        print(
            f"OOF fold {fold}: trained through {fit_months[-1]:%Y-%m}; "
            f"predicted {len(predict_rows):,} rows from {predict_months[0]:%Y-%m} "
            f"to {predict_months[-1]:%Y-%m}"
        )

    return oof


def train(data_path: Path, holdout_months: int = 4, iterations: int = 600) -> dict:
    data = prepare_data(data_path)
    months = np.array(sorted(data["month"].unique()))
    if len(months) <= holdout_months + 5:
        raise ValueError("Not enough distinct months for the requested holdout.")

    test_months = months[-holdout_months:]
    train_data = data[~data["month"].isin(test_months)].copy()
    test_data = data[data["month"].isin(test_months)].copy()

    print(f"Dataset: {len(data):,} rows, {len(months)} months")
    print(
        f"Train: {len(train_data):,} rows through {train_data['month'].max():%Y-%m}; "
        f"test: {len(test_data):,} rows from {test_data['month'].min():%Y-%m}"
    )

    # Stage 1 final model: all pre-holdout rows.
    stage1 = make_model(iterations)
    stage1.fit(
        train_data[BASE_FEATURES],
        train_data[STAGE1_TARGET],
        cat_features=CAT_FEATURES,
    )
    stage1_test_pred = stage1.predict(test_data[BASE_FEATURES])

    # Stage 2 training inputs use temporal OOF Stage-1 predictions.
    oof = chronological_oof_predictions(train_data, iterations)
    stage2_train = train_data.loc[oof.notna()].copy()
    stage2_train["stage1_predicted_distribution_kg"] = oof.loc[oof.notna()]

    stage2_features = BASE_FEATURES + ["stage1_predicted_distribution_kg"]
    stage2 = make_model(iterations)
    stage2.fit(
        stage2_train[stage2_features],
        stage2_train[STAGE2_TARGET],
        cat_features=CAT_FEATURES,
    )

    # Serving-like evaluation: Stage 1 predictions feed Stage 2 on holdout.
    stage2_test_features = test_data[BASE_FEATURES].copy()
    stage2_test_features["stage1_predicted_distribution_kg"] = stage1_test_pred
    stage2_test_pred = stage2.predict(stage2_test_features)

    # Save portable model files and a feature/validation manifest.
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    stage1.save_model(str(MODEL_DIR / "stage1_distribution.cbm"))
    stage2.save_model(str(MODEL_DIR / "stage2_wastage.cbm"))

    results = {
        "dataset_rows": int(len(data)),
        "train_rows": int(len(train_data)),
        "stage2_oof_train_rows": int(len(stage2_train)),
        "test_rows": int(len(test_data)),
        "train_period": [
            train_data["month"].min().strftime("%Y-%m"),
            train_data["month"].max().strftime("%Y-%m"),
        ],
        "test_period": [
            test_data["month"].min().strftime("%Y-%m"),
            test_data["month"].max().strftime("%Y-%m"),
        ],
        "stage1_distribution": metric_pack(
            test_data[STAGE1_TARGET], stage1_test_pred
        ),
        "stage2_wastage": metric_pack(
            test_data[STAGE2_TARGET], stage2_test_pred
        ),
        "base_features": BASE_FEATURES,
        "categorical_features": CAT_FEATURES,
        "stage2_features": stage2_features,
        "note": (
            "Chronological holdout. Stage 2 trained on expanding-window OOF "
            "Stage-1 predictions. Input estimates must be available before "
            "the prediction period; actual closing stock, actual wastage, "
            "wastage percentage, risk level and damaged stock are excluded."
        ),
    }
    (MODEL_DIR / "metrics.json").write_text(json.dumps(results, indent=2))
    print("\nEvaluation:")
    print(json.dumps(results, indent=2))
    print(f"\nSaved models and metrics under: {MODEL_DIR}")
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=ROOT / "data/raw/Datasetfood.csv")
    parser.add_argument("--holdout-months", type=int, default=4)
    parser.add_argument("--iterations", type=int, default=600)
    args = parser.parse_args()
    train(args.data, args.holdout_months, args.iterations)


if __name__ == "__main__":
    main()
