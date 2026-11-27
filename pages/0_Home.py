import streamlit as st

from utils.data_loader import load_dataset
from utils.theme import apply_theme

st.set_page_config(page_title="Food Waste Analysis", page_icon="🍚", layout="wide")
apply_theme()

st.markdown("""
<style>
.block-container {
    padding-top: 3.5rem !important;
}

.hero-panel {
    position: relative;
    overflow: hidden;
    box-sizing: border-box;
    width: 100%;
    padding: 34px 34px 30px;
    border-radius: 22px;
    background: linear-gradient(120deg, rgba(14,165,233,.20), rgba(124,58,237,.22), rgba(236,72,153,.13));
    border: 1px solid rgba(190, 210, 255, .28);
    box-shadow: 0 16px 44px rgba(2, 8, 23, .30), inset 0 1px 0 rgba(255,255,255,.12);
    backdrop-filter: blur(24px) saturate(160%);
    -webkit-backdrop-filter: blur(24px) saturate(160%);
    margin: 8px 0 22px 0;
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

/* Home page navigation cards and their individual rounded buttons */
.st-key-home_dashboard_link_card,
.st-key-home_prediction_link_card {
    background: linear-gradient(135deg, rgba(20, 48, 76, .78), rgba(38, 28, 68, .78)) !important;
    border: 1px solid rgba(125, 211, 252, .34) !important;
    border-radius: 20px !important;
    padding: 18px 20px !important;
}
.st-key-home_dashboard_link_card [data-testid="stPageLink"] a,
.st-key-home_prediction_link_card [data-testid="stPageLink"] a {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-height: 48px;
    padding: 10px 16px !important;
    border-radius: 14px !important;
    border: 1px solid rgba(125, 211, 252, .58) !important;
    background: linear-gradient(110deg, #087eaa, #5141a5) !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    font-weight: 750 !important;
    text-decoration: none !important;
    transition: transform .2s ease, filter .2s ease, border-color .2s ease;
}
.st-key-home_dashboard_link_card [data-testid="stPageLink"] a:hover,
.st-key-home_prediction_link_card [data-testid="stPageLink"] a:hover {
    background: linear-gradient(110deg, #0b9ac7, #684fc5) !important;
    border-color: rgba(186, 230, 253, .9) !important;
    filter: brightness(1.08);
    transform: translateY(-2px);
}
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
    block_count = data.loc[
        data["block"].astype(str).str.upper() != "UNKNOWN", "block"
    ].nunique()

    metrics = [
        ("Records", len(data)),
        ("States", data["state"].nunique()),
        ("Districts", data["district"].nunique()),
        ("Blocks", block_count),
    ]
    metric_cards = "".join(
        f'<div class="stat-card"><div class="stat-label">{label}</div>'
        f'<div class="stat-number" data-target="{int(value)}">0</div></div>'
        for label, value in metrics
    )
    metrics_html = f"""
    <div class="stats-grid">{metric_cards}</div>
    <style>
      * {{ box-sizing: border-box; }}
      body {{ margin: 0; background: transparent; font-family: sans-serif; }}
      .stats-grid {{
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 14px;
      }}
      .stat-card {{
        min-width: 0; min-height: 105px; padding: 16px 18px;
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(14,165,233,.19), rgba(124,58,237,.20), rgba(236,72,153,.12));
        border: 1px solid rgba(190,210,255,.27);
        backdrop-filter: blur(22px) saturate(155%);
        opacity: 0;
        transform: translateX(-28px) scale(.97);
      }}
      .stat-card.is-visible {{
        animation: statSlideIn .48s cubic-bezier(.2,.75,.25,1) forwards;
      }}
      @keyframes statSlideIn {{
        from {{ opacity: 0; transform: translateX(-28px) scale(.97); }}
        to {{ opacity: 1; transform: translateX(0) scale(1); }}
      }}
      .stat-label {{ color: #cbd5e1; font-size: .92rem; font-weight: 650; margin-bottom: 8px; }}
      .stat-number {{ color: #f8fafc; font-size: 2.15rem; font-weight: 750; line-height: 1.1; font-variant-numeric: tabular-nums; }}
      @media (max-width: 700px) {{
        .stats-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }}
        .stat-card {{ min-height: 100px; padding: 14px; }}
        .stat-number {{ font-size: 1.8rem; }}
      }}
      @media (prefers-reduced-motion: reduce) {{
        .stat-card {{ opacity: 1; transform: none; }}
        .stat-card.is-visible {{ animation: none; }}
      }}
    </style>
    <script>
      function syncMetricFrameHeight() {{
        const mobile = window.matchMedia("(max-width: 700px)").matches;
        window.parent.postMessage({{
          isStreamlitMessage: true,
          type: "streamlit:setFrameHeight",
          height: mobile ? 225 : 125
        }}, "*");
      }}
      syncMetricFrameHeight();
      window.addEventListener("resize", syncMetricFrameHeight);

      const cards = Array.from(document.querySelectorAll(".stat-card"));
      const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      function countUp(element) {{
        const target = Number(element.dataset.target);
        const start = performance.now();
        const duration = 1500;
        function tick(now) {{
          const progress = Math.min((now - start) / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          element.textContent = Math.floor(target * eased).toLocaleString("en-IN");
          if (progress < 1) requestAnimationFrame(tick);
        }}
        requestAnimationFrame(tick);
      }}
      if (reduced) {{
        cards.forEach(card => {{
          card.classList.add("is-visible");
          const number = card.querySelector(".stat-number");
          number.textContent = Number(number.dataset.target).toLocaleString("en-IN");
        }});
      }} else {{
        function reveal(index) {{
          if (index >= cards.length) return;
          const card = cards[index];
          card.classList.add("is-visible");
          const number = card.querySelector(".stat-number");
          window.setTimeout(() => countUp(number), 180);
          window.setTimeout(() => reveal(index + 1), 300);
        }}
        reveal(0);
      }}
    </script>
    """
    st.components.v1.html(metrics_html, height=125, scrolling=False)
    st.caption("Location dropdowns show only states, districts and blocks represented in this dataset.")

st.divider()

# Keep both destinations in separate, clearly visible cards.
left, right = st.columns(2, gap="large")

with left:
    with st.container(border=True, key="home_dashboard_link_card"):
        st.subheader("📊 Dashboard")
        st.write("Explore the dataset and its geographic coverage.")
        st.page_link(
            "pages/1_Dashboard.py",
            label="Open Dashboard",
            icon="📊",
            use_container_width=True,
        )

with right:
    with st.container(border=True, key="home_prediction_link_card"):
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

