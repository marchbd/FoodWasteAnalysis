import streamlit as st

from utils.data_loader import load_dataset
from utils.theme import apply_theme

st.set_page_config(page_title="Food Waste Analysis", page_icon="🍚", layout="wide")
apply_theme()

st.markdown("""
<style>
.hero-panel {
    position: relative;
    overflow: hidden;
    padding: 30px 34px;
    border-radius: 22px;
    background: linear-gradient(120deg, rgba(14,165,233,.20), rgba(124,58,237,.22), rgba(236,72,153,.13));
    border: 1px solid rgba(190, 210, 255, .28);
    box-shadow: 0 16px 44px rgba(2, 8, 23, .30), inset 0 1px 0 rgba(255,255,255,.12);
    backdrop-filter: blur(24px) saturate(160%);
    -webkit-backdrop-filter: blur(24px) saturate(160%);
    margin: 4px 0 22px 0;
}
.hero-panel:after {
    content: "";
    position: absolute;
    width: 240px; height: 240px;
    right: -55px; top: -115px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(56,189,248,.32), transparent 68%);
    animation: heroPulse 4s ease-in-out infinite alternate;
}
.hero-title {
    color: #f8fafc; font-size: clamp(2rem, 4vw, 3.15rem);
    font-weight: 800; letter-spacing: -1.5px; margin: 0 0 8px 0;
}
.hero-subtitle { color: #cbd5e1; font-size: 1.04rem; margin: 0 0 20px 0; }
.stage-row { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
.stage-pill {
    display: inline-block; padding: 8px 14px; border-radius: 999px;
    color: #e0f2fe; background: rgba(14,165,233,.16);
    border: 1px solid rgba(125,211,252,.32); font-size: .9rem; font-weight: 650;
}
.stage-arrow { color: #7dd3fc; font-size: 1.2rem; }
@keyframes heroPulse { from { transform: scale(.85); opacity: .55; } to { transform: scale(1.12); opacity: 1; } }
.stat-card {
    min-height: 105px; box-sizing: border-box; padding: 16px 18px;
    border-radius: 16px; background: linear-gradient(145deg, #1e293b, #111827);
    border: 1px solid rgba(148,163,184,.22);
    box-shadow: 0 7px 22px rgba(0,0,0,.16);
}
.stat-label { color: #cbd5e1; font-size: .92rem; font-weight: 650; margin-bottom: 8px; }
.stat-number { color: #f8fafc; font-size: 2.15rem; font-weight: 750; line-height: 1.1; }
</style>
<div class="hero-panel">
  <div class="hero-title">🍚 Food Waste Analysis</div>
  <p class="hero-subtitle">A smarter look at food distribution and wastage prediction.</p>
  <div class="stage-row">
    <span class="stage-pill">Stage 1 · Distribution prediction</span>
    <span class="stage-arrow">→</span>
    <span class="stage-pill">Stage 2 · Wastage prediction</span>
  </div>
</div>
""", unsafe_allow_html=True)

data = load_dataset()
if data is None:
    st.warning("Dataset missing. Add data/raw/Datasetfood.csv to the repository.")
else:
    def animated_count(label, value):
        html = """
        <div class="stat-card">
          <div class="stat-label">__LABEL__</div>
          <div class="stat-number"><span id="count">0</span></div>
        </div>
        <style>
          body { margin: 0; background: transparent; }
          .stat-card { min-height: 105px; box-sizing: border-box; padding: 16px 18px;
            border-radius: 16px; background: linear-gradient(135deg, rgba(14,165,233,.19), rgba(124,58,237,.20), rgba(236,72,153,.12));
            border: 1px solid rgba(190,210,255,.27); backdrop-filter: blur(22px) saturate(155%); }
          .stat-label { color: #cbd5e1; font: 650 .92rem sans-serif; margin-bottom: 8px; }
          .stat-number { color: #f8fafc; font: 750 2.15rem/1.1 sans-serif; }
        </style>
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
        """.replace("__VALUE__", str(int(value))).replace("__LABEL__", label)
        st.components.v1.html(html, height=112, scrolling=False)

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

# Keep both destinations in separate, clearly visible cards.
left, right = st.columns(2, gap="large")

with left:
    with st.container(border=True):
        st.subheader("📊 Dashboard")
        st.write("Explore the dataset and its geographic coverage.")
        st.page_link(
            "pages/1_Dashboard.py",
            label="Open Dashboard",
            icon="📊",
            use_container_width=True,
        )

with right:
    with st.container(border=True):
        st.subheader("🔮 Food Waste Prediction")
        st.write(
            "Choose a state and district with available data. "
            "Block selection is optional."
        )
        st.page_link(
            "pages/2_Food_Waste_Prediction.py",
            label="Open Prediction",
            icon="🔮",
            use_container_width=True,
        )

