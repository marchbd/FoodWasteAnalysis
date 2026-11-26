import streamlit as st

from utils.data_loader import load_dataset
from prediction.pipeline import models_ready

st.set_page_config(page_title="Food Waste Analysis", page_icon="🍚", layout="wide")

st.title("🍚 Food Waste Analysis")
st.caption("A two-stage machine learning system for food distribution and wastage prediction.")
st.markdown(
    "**Stage 1 — Distribution prediction** → **Stage 2 — Wastage prediction**\n\n"
    "This project uses a synthetic dataset for model experimentation. Its generated "
    "values are illustrative and are not official statistics."
)

data = load_dataset()
if data is None:
    st.warning("Dataset missing. Add data/raw/Datasetfood.csv to the repository.")
else:
    def animated_count(label, value):
        st.markdown(f"**{label}**")
        html = """
        <div style="font-family: sans-serif; font-size: 2.25rem; line-height: 1.25; color: #FAFAFA; font-weight: 400;">
          <span id="count">0</span>
        </div>
        <script>
          const target = __VALUE__;
          const duration = 1500;
          const start = performance.now();
          const number = document.getElementById("count");
          function animate(now) {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            number.textContent = Math.floor(target * eased).toLocaleString("en-IN");
            if (progress < 1) requestAnimationFrame(animate);
          }
          requestAnimationFrame(animate);
        </script>
        """.replace("__VALUE__", str(int(value)))
        st.components.v1.html(html, height=58, scrolling=False)

    block_count = data.loc[
        data["block"].astype(str).str.upper() != "UNKNOWN", "block"
    ].nunique()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        animated_count("Records", len(data))
    with c2:
        animated_count("States", data["state"].nunique())
    with c3:
        animated_count("Districts", data["district"].nunique())
    with c4:
        animated_count("Blocks", block_count)
    st.caption("Location dropdowns show only states, districts and blocks represented in this dataset.")

st.divider()
left, right = st.columns(2)
with left:
    st.subheader("📊 Dashboard")
    st.write("Explore the dataset and its geographic coverage.")
    st.page_link("pages/1_Dashboard.py", label="Open Dashboard", icon="📊")
with right:
    st.subheader("🔮 Food Waste Prediction")
    st.write("Choose a state and district with available data. Block selection is optional.")
    st.page_link("pages/2_Food_Waste_Prediction.py", label="Open Prediction", icon="🔮")

if models_ready():
    st.success("Both prediction models are available.")
else:
    st.warning("Prediction models are missing. Add both .cbm files under models/.")

