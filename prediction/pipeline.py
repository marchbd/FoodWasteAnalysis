"""Load the trained CatBoost models committed in the repository."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from catboost import CatBoostRegressor

ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT / "models"
BASE_FEATURES = [
    "shop_id", "state", "district", "block", "commodity",
    "year", "month_number", "opening_stock_kg", "received_stock_kg",
    "beneficiaries", "transactions", "storage_capacity_kg",
    "storage_days", "delivery_delay_days", "previous_wastage_kg",
]
STAGE2_FEATURES = BASE_FEATURES + ["stage1_predicted_distribution_kg"]


def _model_path(filename: str) -> Path:
    path = MODEL_DIR / filename
    if not path.is_file():
        raise FileNotFoundError(
            f"Required model file not found: {path}. "
            "Check that the trained model files are committed under models/."
        )
    return path


def models_ready() -> bool:
    return all(
        (MODEL_DIR / name).is_file()
        for name in ("stage1_distribution.cbm", "stage2_wastage.cbm")
    )


def load_models() -> tuple[CatBoostRegressor, CatBoostRegressor]:
    distribution, wastage = CatBoostRegressor(), CatBoostRegressor()
    distribution.load_model(str(_model_path("stage1_distribution.cbm")))
    wastage.load_model(str(_model_path("stage2_wastage.cbm")))
    return distribution, wastage


def predict_food_waste(inputs: dict) -> dict[str, float]:
    required = set(BASE_FEATURES) - {"year", "month_number"}
    missing = sorted(required - set(inputs))
    if missing:
        raise ValueError(f"Missing prediction inputs: {missing}")
    period = pd.Period(str(inputs["prediction_month"]), freq="M")
    row = {key: inputs[key] for key in required}
    row["year"], row["month_number"] = int(period.year), int(period.month)
    frame = pd.DataFrame([row], columns=BASE_FEATURES)
    distribution_model, wastage_model = load_models()
    predicted_distribution = max(0.0, float(distribution_model.predict(frame)[0]))
    stage2_frame = frame.copy()
    stage2_frame["stage1_predicted_distribution_kg"] = predicted_distribution
    predicted_wastage = max(0.0, float(wastage_model.predict(stage2_frame[STAGE2_FEATURES])[0]))
    return {
        "predicted_distributed_stock_kg": round(predicted_distribution, 2),
        "predicted_wastage_kg": round(predicted_wastage, 2),
    }


def load_metrics() -> dict | None:
    try:
        return json.loads(_model_path("metrics.json").read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return None
