from pathlib import Path

import streamlit as st

from utils.data_loader import load_dataset

ROOT_DIR = Path(__file__).resolve().parent

st.set_page_config(
    page_title="Food Waste Analysis",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        .block-container { padding-top: 2rem; padding-bottom: 3rem; }
        [data-testid="stMetric"] {
            background: rgba(128, 128, 128, 0.08);
            border: 1px solid rgba(128, 128, 128, 0.18);
            padding: 1rem;
            border-radius: 0.8rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🍚 Food Waste Analysis")
st.caption("An ML-powered system for food distribution and wastage prediction.")

st.markdown(
    """
    Welcome to the Food Waste Analysis platform. The planned prediction workflow
    uses two connected machine-learning stages:

    **Stage 1 — Distribution prediction** → **Stage 2 — Wastage prediction**
    """
)

dataset = load_dataset()

if dataset is None:
    st.info(
        "The dataset has not been added yet. Place your CSV at "
        "data/raw/Datasetfood.csv to enable dataset-based dashboard summaries."
    )
else:
    left, middle, right = st.columns(3)
    left.metric("Dataset records", f"{len(dataset):,}")
    middle.metric("Dataset columns", len(dataset.columns))
    right.metric("Dataset status", "Ready")

st.divider()
st.subheader("Explore the application")
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📊 Dashboard")
    st.write("Review dataset availability and high-level food stock information.")
    st.page_link("pages/1_Dashboard.py", label="Open Dashboard", icon="📊")
with col2:
    st.markdown("### 🔮 Food Waste Prediction")
    st.write("Enter shop and stock information for the planned two-stage prediction.")
    st.page_link("pages/2_Food_Waste_Prediction.py", label="Open Prediction", icon="🔮")

st.warning(
    "Predictions are not enabled yet. We will activate them only after training "
    "and validating both models against the project dataset."
)
