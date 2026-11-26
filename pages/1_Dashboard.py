import streamlit as st
from utils.data_loader import load_dataset
from prediction.pipeline import load_metrics

st.title("📊 Food Waste Demo Dashboard")
st.caption("Geographic coverage and records in the synthetic demonstration dataset.")

data = load_dataset()
if data is None:
    st.error("Demo dataset missing. Add data/raw/Datasetfood.csv.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Records", f"{len(data):,}")
c2.metric("States", data["state"].nunique())
c3.metric("Districts", data["district"].nunique())
c4.metric("Blocks", data.loc[data["block"].astype(str).str.upper() != "UNKNOWN", "block"].nunique())

st.info("Dropdown options are derived from this dataset. A missing district or block means this demo dataset has no record for that location; it does not mean the place does not exist.")
st.warning("All stock, distribution and wastage values in this dataset are synthetic demonstration values, not official government records.")

st.subheader("Geographic coverage")
coverage = (
    data[data["block"].astype(str).str.upper() != "UNKNOWN"]
    .groupby("state", as_index=False)
    .agg(districts=("district", "nunique"), blocks=("block", "nunique"), records=("state", "size"))
    .sort_values("state")
)
st.dataframe(coverage, use_container_width=True, hide_index=True)

st.subheader("Dataset preview")
st.dataframe(data.head(30), use_container_width=True)

st.subheader("Records by state")
state_counts = data.groupby("state").size().sort_values(ascending=False)
st.bar_chart(state_counts)

metrics = load_metrics()
if metrics:
    st.divider()
    st.subheader("Synthetic-model chronological evaluation")
    st.caption(f"Train: {metrics['train_period'][0]} to {metrics['train_period'][1]} · Test: {metrics['test_period'][0]} to {metrics['test_period'][1]}")
    a, b = st.columns(2)
    a.metric("Distribution MAE", f"{metrics['stage1_distribution']['mae']:,.2f} kg")
    b.metric("Wastage MAE", f"{metrics['stage2_wastage']['mae']:,.2f} kg")
    st.warning("These scores measure fit to synthetic demo data only, not accuracy on real distribution-system data.")
