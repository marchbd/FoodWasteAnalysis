# Food Waste Analysis

An ML-based food waste analysis and prediction system built with Python and Streamlit.

The project is designed around a **two-stage regression pipeline**:

1. **Distribution model:** predicts the quantity of food distributed from information available before the prediction period.
2. **Wastage model:** uses the original inputs plus the Stage 1 predicted distribution to predict food wastage.

> The models are not trained yet. This commit establishes the application scaffold; prediction pages will be connected after the dataset audit and leakage-safe model training.

## Project structure

    FoodWasteAnalysis/
    ├── app.py
    ├── requirements.txt
    ├── data/
    │   ├── raw/                 # Put Datasetfood.csv here (kept out of Git)
    │   └── processed/           # Generated cleaned data (kept out of Git)
    ├── models/                  # Trained model artifacts (kept out of Git)
    ├── training/                # Preprocessing, training and evaluation
    ├── prediction/              # Two-stage inference pipeline
    ├── pages/                   # Streamlit pages
    ├── utils/                   # Shared data and UI helpers
    └── assets/                  # Images and styles

## Local setup (Windows PowerShell)

    git clone https://github.com/marchbd/FoodWasteAnalysis.git
    cd FoodWasteAnalysis
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt

Place the source dataset at data/raw/Datasetfood.csv, then run:

    streamlit run app.py

## Current status

- [x] Initial Streamlit application scaffold
- [x] Multipage navigation
- [x] Dataset loading helper
- [ ] Dataset audit and feature/target verification
- [ ] Stage 1 distribution model
- [ ] Stage 2 wastage model with out-of-fold Stage 1 predictions
- [ ] Model evaluation and prediction integration
- [ ] Analysis charts, risk insights and downloadable reports

## Important modelling rule

Only features genuinely available at the time of a future prediction may be used as inputs. The second-stage model must be trained on out-of-fold Stage 1 predictions (rather than only actual distribution values) to reduce training-serving mismatch. Target-derived fields such as actual wastage percentage or risk labels must not leak into model inputs.
