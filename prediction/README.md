# Prediction pipeline

The live inference flow will be:

1. Validate user inputs.
2. Load the Stage 1 distribution model and predict distributed quantity.
3. Add the predicted distribution to the original feature set.
4. Load the Stage 2 wastage model and predict wastage.
5. Return both predictions and derived metrics to the Streamlit page.

Model loading and prediction functions will be implemented after training and feature schemas are finalized.
