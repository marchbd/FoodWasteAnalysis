# Food Waste Analysis

A two-stage machine-learning application for estimating monthly food distribution and food wastage at fair-price shops.

## Workflow

1. Stage 1 predicts distributed quantity (`distributed_stock_kg`).
2. Stage 2 predicts wastage (`wastage_kg`) using the original prediction-time inputs plus Stage 1's predicted distribution.
3. Stage 2 is trained with expanding-window out-of-fold Stage-1 predictions to reduce training/serving mismatch.

## Dataset

Place the source CSV at `data/raw/Datasetfood.csv` to retrain locally. The CSV is not committed to GitHub.

Audited dataset: 57,639 rows, 20 columns, 34 monthly periods (2024-01 to 2026-10), with no missing values or duplicate rows.

## Model artifacts

The trained CatBoost model files and evaluation metrics are stored directly in this repository under `models/`:

- `models/stage1_distribution.cbm`
- `models/stage2_wastage.cbm`
- `models/metrics.json`

The prediction pipeline loads these files from the repository's local checkout. No Hugging Face account, model repository, or secret is required.

## Run locally

```powershell
git clone https://github.com/marchbd/FoodWasteAnalysis.git
cd FoodWasteAnalysis
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

To retrain, place `Datasetfood.csv` at `data/raw/Datasetfood.csv`, then run `python -m training.train_models`.

## Deploy

1. Open [Streamlit Community Cloud](https://share.streamlit.io/).
2. Create a new app from `marchbd/FoodWasteAnalysis`, branch `main`, with `app.py` as the entry point.
3. Deploy. No model-hosting secret is needed because the model files are committed in `models/`.

## Important modelling note

Do not use actual closing stock, actual wastage, wastage percentage, risk level, or damaged stock as future prediction inputs. Input estimates must represent information available before the month being predicted.
