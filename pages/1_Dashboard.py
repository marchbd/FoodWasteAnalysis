import streamlit as st

from prediction.pipeline import load_metrics
from utils.data_loader import load_dataset

st.title("📊 Food Waste Dashboard")
st.caption("Dataset overview and model validation.")

data = load_dataset()
if data is not None:
    first, second, third = st.columns(3)
    first.metric("Records", f"{len(data):,}")
    second.metric("Features", len(data.columns))
    third.metric("Missing cells", f"{int(data.isna().sum().sum()):,}")

    st.subheader("Dataset preview")
    st.dataframe(data.head(20), use_container_width=True)

    st.subheader("Missing values by column")
    missing = data.isna().sum().sort_values(ascending=False)
    missing = missing[missing > 0]
    if missing.empty:
        st.success("No missing values found.")
    else:
        st.bar_chart(missing)
else:
    st.info("The raw CSV is not bundled with the deployed app. Model predictions and validation metrics remain available without it.")

metrics = load_metrics()
if metrics:
    st.divider()
    st.subheader("Chronological model validation")
    st.caption(
        f"Training: {metrics['train_period'][0]} to {metrics['train_period'][1]} · "
        f"Testing: {metrics['test_period'][0]} to {metrics['test_period'][1]}"
    )
    left, right = st.columns(2)
    left.metric("Distribution MAE", f"{metrics['stage1_distribution']['mae']:,.2f} kg")
    right.metric("Wastage MAE", f"{metrics['stage2_wastage']['mae']:,.2f} kg")
    with st.expander("Full evaluation metrics"):
        st.json({
            "Stage 1 — Distribution": metrics["stage1_distribution"],
            "Stage 2 — Wastage": metrics["stage2_wastage"],
            "Test records": metrics["test_rows"],
            "Stage 2 OOF training records": metrics["stage2_oof_train_rows"],
        })
else:
    st.warning("Validation metrics will appear after the models are trained.")
