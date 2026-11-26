# Food Waste Analysis — Generated Data Project

A two-stage CatBoost demonstration application:
1. Stage 1 predicts distributed quantity.
2. Stage 2 predicts wastage using Stage 1's predicted distribution.

## Dataset

The generated dataset is `data/raw/Datasetfood.csv` (40,720 rows, 19 columns), covering 12 states, 51 districts, and 209 named blocks from 2024-01 through 2026-10. It contains five commodities. A subset of rows uses `block=UNKNOWN` to train and test the optional-block prediction path.

**All numeric stock, demand, distribution and wastage values are generated.** Administrative names are taken from the geographic combinations present in the supplied source dataset. Missing dropdown entries mean no record exists in this dataset; they do not indicate that a real place does not exist.

## Location selectors

The State dropdown is populated from distinct `state` values in the CSV. District options are filtered by the selected state. Block options are filtered by selected state and district, and only named blocks with records are shown. Block can be skipped; the pipeline then supplies `UNKNOWN`.

## Features and targets

No `shop_id` column is used. Model features include state, district, block, commodity, month components, opening/received stock, beneficiaries, transactions, capacity, storage duration, delivery delay, and previous wastage. Leakage columns such as actual closing stock, wastage, wastage percentage, risk level, and damaged stock are not model inputs.

## Train locally

```powershell
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python -m training.train_models --data data/raw/Datasetfood.csv --holdout-months 4 --iterations 450
streamlit run app.py
```

## Deployment

Deploy `app.py` from branch `main` on Streamlit Community Cloud. No Hugging Face account or secrets are required. Commit the dataset CSV to `data/raw/Datasetfood.csv` and the two trained model files to `models/`.

## Evaluation warning

The chronological holdout scores in `models/metrics.json` are calculated on generated data. They demonstrate the pipeline and are not evidence of real-world predictive accuracy.
