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

The trained model files and `metrics.json` are hosted in a public Hugging Face model repository.

Expected files:
- `stage1_distribution.cbm`
- `stage2_wastage.cbm`
- `metrics.json`

Set this secret in Streamlit Community Cloud → App settings → Secrets:

```toml
HF_MODEL_REPO_ID = "your-huggingface-username/foodwaste-models"
```

The app downloads the files automatically and caches them.

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

1. Create a public model repository on Hugging Face and upload the three files listed above.
2. Deploy `marchbd/FoodWasteAnalysis` from [Streamlit Community Cloud](https://share.streamlit.io/).
3. Add the `HF_MODEL_REPO_ID` secret shown above.

## Important modelling note

Do not use actual closing stock, actual wastage, wastage percentage, risk level, or damaged stock as future prediction inputs. Input estimates must represent information available before the month being predicted.
