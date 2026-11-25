# Food Waste Analysis

A two-stage machine-learning project for estimating monthly food distribution and food wastage at fair-price shops.

## Workflow

1. Stage 1 predicts distributed quantity (`distributed_stock_kg`).
2. Stage 2 predicts wastage (`wastage_kg`) using the original prediction-time inputs plus Stage 1's predicted distribution.

Stage 2 is trained with expanding-window out-of-fold Stage-1 predictions to reduce the training/serving mismatch.

## Dataset

Place the original file at `data/raw/Datasetfood.csv`. The dataset is not committed to GitHub; raw CSVs and trained model artifacts are ignored by Git.

Audited dataset: 57,639 rows, 20 columns, 34 monthly periods (2024-01 to 2026-10), 7,494 shop IDs, 12 states, 51 districts, 209 blocks, Rice and Wheat. No missing values or duplicate rows were found.

## Run locally

```powershell
git clone https://github.com/marchbd/FoodWasteAnalysis.git
cd FoodWasteAnalysis
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Copy `Datasetfood.csv` into `data/raw/`, then train:

```powershell
python -m training.train_models
```

Launch the website:

```powershell
streamlit run app.py
```

## Important modelling note

Do not use actual closing stock, actual wastage, wastage percentage, risk level, or damaged stock as future prediction inputs. These are observed outcomes or potentially unavailable at forecast time. Input estimates must represent information available before the month being predicted.

See [training/README.md](training/README.md) for validation details.


## Current validation run

A 300-iteration CatBoost run used a chronological holdout of July–October 2026 (2,472 test records). Stage 1 distribution: MAE 170.7559 kg, RMSE 214.7875 kg, R² 0.94216. Stage 2 wastage: MAE 25.3439 kg, RMSE 36.3381 kg, R² 0.86554. Metrics are stored in `models/metrics.json`. These results are specific to this run and should be regenerated after changing features or training settings.

## Deploy on Streamlit Community Cloud

1. Ensure `models/stage1_distribution.cbm` and `models/stage2_wastage.cbm` are present in the repository's `models/` folder, alongside `models/metrics.json`.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Choose **Create app**, select this repository, branch `main`, and main file `app.py`.
4. Deploy the app. The raw CSV is not required for prediction once the trained model files are present; it is only used for the optional dataset preview on the dashboard.
