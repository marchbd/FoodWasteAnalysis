# Model training

The dataset audit found 57,639 rows across 34 monthly periods (2024-01 to 2026-10), with no missing values or duplicate rows.

## Train the models

1. Put the original CSV at `data/raw/Datasetfood.csv`.
2. Install dependencies with `pip install -r requirements.txt`.
3. From the repository root, run:

```bash
python -m training.train_models
```

Optional arguments:

```bash
python -m training.train_models --data data/raw/Datasetfood.csv --holdout-months 4 --iterations 600
```

The script:
- Holds out the latest four months as a chronological test set.
- Trains Stage 1 to predict `distributed_stock_kg`.
- Creates expanding-window out-of-fold Stage-1 predictions for Stage-2 training.
- Trains Stage 2 to predict `wastage_kg` from the original prediction-time features plus the OOF distribution prediction.
- Evaluates the serving-like two-stage flow on the held-out months.
- Saves two CatBoost models and `metrics.json` under `models/`.

## Feature availability and leakage

The models intentionally exclude `actual_closing_stock_kg`, `wastage_kg`, `wastage_percent`, `risk_level`, and `damaged_stock_kg` from inputs. Those fields are observed outcomes or may only be known after the prediction period.

Beneficiaries, transactions, received stock, storage duration, and delivery delay must be supplied as estimates/known values for the month being forecast. If the real deployment cannot know a field before the forecast, remove it from both the feature list and input form and retrain.

The dataset contains 34 months and 7,494 distinct shop IDs. Shop IDs are categorical features; predictions for entirely new shops may be less reliable.
