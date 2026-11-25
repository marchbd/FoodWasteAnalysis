# Model training

Training scripts will be added after the dataset schema and target definitions are audited.

Planned sequence:

1. Validate columns, types, missing values, duplicates and temporal coverage.
2. Define only prediction-time-available features.
3. Split data chronologically for evaluation.
4. Train Stage 1 to predict the dataset's distributed-quantity target.
5. Generate out-of-fold Stage 1 predictions for Stage 2 training.
6. Train Stage 2 to predict actual wastage using original features plus out-of-fold predicted distribution.
7. Evaluate both stages and save model artifacts under models/.

Do not train Stage 2 only on actual distribution and then serve it predicted distribution without addressing the training-serving mismatch.
