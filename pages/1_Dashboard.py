import streamlit as st

from utils.data_loader import load_dataset

st.title("📊 Food Waste Dashboard")
st.caption("Dataset overview and exploratory analysis.")

data = load_dataset()
if data is None:
    st.info("Add data/raw/Datasetfood.csv to enable dashboard analysis.")
    st.stop()

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
