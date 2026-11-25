# Food Waste Analysis

A two-stage machine-learning application for estimating monthly food distribution and food wastage at fair-price shops. The trained models do not use shop IDs. State and District are required prediction inputs; Block is optional.

## Workflow

1. Stage 1 predicts distributed quantity (`distributed_stock_kg`).
2. Stage 2 predicts wastage (`wastage_kg`) using the original prediction-time inputs plus Stage 1's predicted distribution.
3. Stage 2 is trained with expanding-window out-of-fold Stage 1 predictions to reduce training/serving mismatch.

## Dataset

Place the original source CSV at `data/raw/Datasetfood.csv` to retrain locally. The committed all-India sample dataset is synthetic and intended only for dashboard demonstration; do not use it for model training or as real government statistics.

## Model artifacts

The trained CatBoost model files and evaluation metrics are stored under `models/`:

- `models/stage1_distribution.cbm`
- `models/stage2_wastage.cbm`
- `models/metrics.json`

The prediction pipeline loads these files from the repository's local checkout. No Hugging Face account, model repository, or secret is required.

## Prediction inputs

- State and District are required.
- Block is optional. If omitted, the pipeline supplies `UNKNOWN`.
- Shop ID is not used by either model.

## Run locally

```powershell
git clone https://github.com/marchbd/FoodWasteAnalysis.git
cd FoodWasteAnalysis
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

To retrain, use the original dataset at `data/raw/Datasetfood.csv`, then run `python -m training.train_models`. The committed synthetic dashboard CSV is not suitable for retraining.

## Deploy

1. Open [Streamlit Community Cloud](https://share.streamlit.io/).
2. Create or manage the app from `marchbd/FoodWasteAnalysis`, branch `main`, with `app.py` as the entry point.
3. Deploy. No model-hosting secret is needed because the model files are committed in `models/`.

## Validation

The reported metrics use a chronological four-month holdout. See `models/metrics.json` for the results and the same-iteration comparison with the previous shop-ID feature set. These are offline evaluation results, not a guarantee of production accuracy.

Do not use actual closing stock, actual wastage, wastage percentage, risk level, or damaged stock as future prediction inputs. Inputs must represent information available before the month being predicted.
