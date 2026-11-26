import streamlit as st
from utils.data_loader import load_dataset
from utils.theme import apply_theme

apply_theme()

st.title("📊 Food Waste Dashboard")
st.caption("Geographic coverage and records across the dataset.")

data = load_dataset()
if data is None:
    st.error("Dataset missing. Add data/raw/Datasetfood.csv.")
    st.stop()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Records", f"{len(data):,}")
c2.metric("States", data["state"].nunique())
c3.metric("Districts", data["district"].nunique())
c4.metric("Blocks", data.loc[data["block"].astype(str).str.upper() != "UNKNOWN", "block"].nunique())


st.subheader("Geographic coverage")
coverage = (
    data[data["block"].astype(str).str.upper() != "UNKNOWN"]
    .groupby("state", as_index=False)
    .agg(districts=("district", "nunique"), blocks=("block", "nunique"), records=("state", "size"))
    .sort_values("state")
)
st.dataframe(coverage, use_container_width=True, hide_index=True)

st.subheader("Records by state")
state_counts = data.groupby("state").size().sort_values(ascending=False)
st.bar_chart(state_counts)

