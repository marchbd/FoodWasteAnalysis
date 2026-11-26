import streamlit as st

from utils.data_loader import load_dataset
from prediction.pipeline import load_metrics, models_ready

st.set_page_config(page_title="Food Waste Analysis", page_icon="🍚", layout="wide")

st.title("🍚 Food Waste Analysis")
st.caption("A two-stage ML demo for food distribution and wastage prediction.")
st.markdown(
    "**Stage 1 — Distribution prediction** → **Stage 2 — Wastage prediction**\n\n"
    "This project currently uses a synthetic demonstration dataset. Its generated "
    "values are for software demonstration and model experimentation, not official statistics."
)

data = load_dataset()
if data is None:
    st.warning("Demo dataset missing. Add data/raw/Datasetfood.csv to the repository.")
else:
    c1, c2, c3 = st.columns(3)
    c1.metric("Demo records", f"{len(data):,}")
    c2.metric("States represented", data["state"].nunique())
    c3.metric("Districts represented", data["district"].nunique())
    st.caption("Location dropdowns show only states, districts and blocks represented in this dataset.")

st.divider()
left, right = st.columns(2)
with left:
    st.subheader("📊 Dashboard")
    st.write("Explore the synthetic demo dataset and its geographic coverage.")
    st.page_link("pages/1_Dashboard.py", label="Open Dashboard", icon="📊")
with right:
    st.subheader("🔮 Food Waste Prediction")
    st.write("Choose a state and district with available data. Block selection is optional.")
    st.page_link("pages/2_Food_Waste_Prediction.py", label="Open Prediction", icon="🔮")

if models_ready():
    st.success("Both demo-trained prediction models are available.")
else:
    st.warning("Prediction models are missing. Add both .cbm files under models/.")

metrics = load_metrics()
if metrics:
    st.subheader("Demo-model validation snapshot")
    c1, c2 = st.columns(2)
    c1.metric("Distribution MAE", f"{metrics['stage1_distribution']['mae']:,.2f} kg")
    c2.metric("Wastage MAE", f"{metrics['stage2_wastage']['mae']:,.2f} kg")
    st.caption(
        f"Synthetic chronological holdout: {metrics['test_period'][0]} to "
        f"{metrics['test_period'][1]} · {metrics['test_rows']:,} records"
    )
