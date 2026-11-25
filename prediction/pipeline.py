"""Load trained models and run the two-stage prediction pipeline."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from catboost import CatBoostRegressor

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"

BASE_FEATURES = [
    "shop_id", "state", "district", "block", "commodity",
    "year", "month_number",
    "opening_stock_kg", "received_stock_kg",
    "beneficiaries", "transactions",
    "storage_capacity_kg", "storage_days",
    "delivery_delay_days", "previous_wastage_kg",
]
STAGE2_FEATURES = BASE_FEATURES + ["stage1_predicted_distribution_kg"]


def models_ready() -> bool:
    return (
        (MODEL_DIR / "stage1_distribution.cbm").exists()
        and (MODEL_DIR / "stage2_wastage.cbm").exists()
    )


def load_models() -> tuple[CatBoostRegressor, CatBoostRegressor]:
    if not models_ready():
        raise FileNotFoundError(
            "Trained models are missing. Run: python -m training.train_models"
        )
    distribution = CatBoostRegressor()
    wastage = CatBoostRegressor()
    distribution.load_model(str(MODEL_DIR / "stage1_distribution.cbm"))
    wastage.load_model(str(MODEL_DIR / "stage2_wastage.cbm"))
    return distribution, wastage


def predict_food_waste(inputs: dict) -> dict[str, float]:
    """inputs must contain all BASE_FEATURES except year/month_number,
    which are derived from prediction_month (YYYY-MM).
    """
    required = set(BASE_FEATURES) - {"year", "month_number"}
    missing = sorted(required - set(inputs))
    if missing:
        raise ValueError(f"Missing prediction inputs: {missing}")

    period = pd.Period(str(inputs["prediction_month"]), freq="M")
    row = {key: inputs[key] for key in required}
    row["year"] = int(period.year)
    row["month_number"] = int(period.month)
    frame = pd.DataFrame([row], columns=BASE_FEATURES)

    distribution_model, wastage_model = load_models()
    predicted_distribution = max(
        0.0, float(distribution_model.predict(frame)[0])
    )

    stage2_frame = frame.copy()
    stage2_frame["stage1_predicted_distribution_kg"] = predicted_distribution
    predicted_wastage = max(
        0.0, float(wastage_model.predict(stage2_frame[STAGE2_FEATURES])[0])
    )

    return {
        "predicted_distributed_stock_kg": round(predicted_distribution, 2),
        "predicted_wastage_kg": round(predicted_wastage, 2),
    }


def load_metrics() -> dict | None:
    path = MODEL_DIR / "metrics.json"
    if not path.exists():
        return None
    return json.loads(path.read_text())
