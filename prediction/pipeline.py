"""Load trained models from local storage or a public Hugging Face model repository."""
from __future__ import annotations
import json, os
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

def _model_repo_id() -> str | None:
    repo_id = os.getenv("HF_MODEL_REPO_ID")
    if repo_id:
        return repo_id.strip() or None
    try:
        import streamlit as st
        return str(st.secrets.get("HF_MODEL_REPO_ID", "")).strip() or None
    except Exception:
        return None

def _resolve_model_file(filename: str) -> Path:
    local_path = MODEL_DIR / filename
    if local_path.exists():
        return local_path
    repo_id = _model_repo_id()
    if not repo_id:
        raise FileNotFoundError(
            "Models are not available. Configure HF_MODEL_REPO_ID with your "
            "public Hugging Face model repository, e.g. 'username/foodwaste-models'."
        )
    from huggingface_hub import hf_hub_download
    return Path(hf_hub_download(repo_id=repo_id, filename=filename, repo_type="model"))

def models_ready() -> bool:
    try:
        _resolve_model_file("stage1_distribution.cbm")
        _resolve_model_file("stage2_wastage.cbm")
        return True
    except Exception:
        return False

def load_models() -> tuple[CatBoostRegressor, CatBoostRegressor]:
    distribution, wastage = CatBoostRegressor(), CatBoostRegressor()
    distribution.load_model(str(_resolve_model_file("stage1_distribution.cbm")))
    wastage.load_model(str(_resolve_model_file("stage2_wastage.cbm")))
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
        return json.loads(_resolve_model_file("metrics.json").read_text(encoding="utf-8"))
    except Exception:
        return None
