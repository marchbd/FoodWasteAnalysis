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
    background: radial-gradient(circle at 88% 12%, rgba(177,156,122,.25), transparent 26%), linear-gradient(115deg, #EED4AC 0%, #F4EBDD 52%, #E7DCCB 100%);
    border: 1px solid #D7C3A5;
    box-shadow: 12px 12px 26px rgba(90,68,52,.13), -9px -9px 22px rgba(255,255,255,.88), inset 1px 1px 0 rgba(255,255,255,.85);
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
    background: radial-gradient(circle, rgba(177,156,122,.42), transparent 68%);
    animation: heroPulse 4s ease-in-out infinite alternate;
}
.hero-title {
    color: #0D0B09; font-size: clamp(2rem, 4vw, 3.15rem);
    font-weight: 800; letter-spacing: -1.5px; margin: 0 0 8px 0;
}
.hero-subtitle { color: #5A4434; font-size: 1.04rem; margin: 0 0 20px 0; }
.stage-row { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }
.stage-pill {
    display: inline-block; padding: 8px 14px; border-radius: 999px;
    color: #5A4434; background: linear-gradient(110deg, #F7E8D0, #EED4AC);
    border: 1px solid #D7C3A5; font-size: .9rem; font-weight: 650;
}
.stage-arrow { color: #2EA334; font-size: 1.2rem; }
@keyframes heroPulse { from { transform: scale(.85); opacity: .55; } to { transform: scale(1.12); opacity: 1; } }
.stat-card {
    min-height: 105px; box-sizing: border-box; padding: 16px 18px;
    border-radius: 16px; background: linear-gradient(145deg, #FFFCF6, #F0E5D4);
    border: 1.5px solid #B9A184;
    box-shadow: 7px 7px 16px rgba(90,68,52,.14), -6px -6px 14px rgba(255,255,255,.88);
    transition: transform .28s ease, box-shadow .28s ease, border-color .28s ease;
}
.stat-card:hover {
    transform: translateY(-7px) scale(1.015);
    border-color: #80674F;
    box-shadow: 12px 16px 24px rgba(90,68,52,.20), -5px -5px 14px rgba(255,255,255,.9);
}
.stat-label { color: #877967; font-size: .92rem; font-weight: 650; margin-bottom: 8px; }
.stat-number { color: #2EA334; font-size: 2.15rem; font-weight: 750; line-height: 1.1; }

/* Home page navigation cards and their individual rounded buttons */
.st-key-home_dashboard_link_card,
.st-key-home_prediction_link_card {
    background: linear-gradient(145deg, #FFFCF6, #F0E5D4) !important;
    border: 1.5px solid #B9A184 !important;
    border-radius: 20px !important;
    box-shadow: 7px 7px 17px rgba(90,68,52,.13), -5px -5px 14px rgba(255,255,255,.82) !important;
    transition: transform .28s ease, box-shadow .28s ease, border-color .28s ease;
    padding: 18px 20px !important;
}
.st-key-home_dashboard_link_card:hover,
.st-key-home_prediction_link_card:hover {
    transform: translateY(-5px);
    border-color: #80674F !important;
    box-shadow: 11px 14px 23px rgba(90,68,52,.20), -5px -5px 14px rgba(255,255,255,.9) !important;
}
.st-key-home_dashboard_link_card [data-testid="stPageLink"] a,
.st-key-home_prediction_link_card [data-testid="stPageLink"] a {
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    min-height: 48px;
    padding: 10px 16px !important;
    border-radius: 14px !important;
    border: 1px solid #25872C !important;
    background: linear-gradient(115deg, #36B33D, #25872C) !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
    font-weight: 750 !important;
    text-decoration: none !important;
    transition: transform .25s ease, filter .25s ease, border-color .25s ease, box-shadow .25s ease;
    box-shadow: 4px 5px 10px rgba(36,93,43,.20);
}
.st-key-home_dashboard_link_card [data-testid="stPageLink"] a {
    background: linear-gradient(115deg, #287A3C, #185B32) !important;
    border-color: #174B2A !important;
}
.st-key-home_prediction_link_card [data-testid="stPageLink"] a {
    background: linear-gradient(115deg, #42B84A, #258C35) !important;
    border-color: #1E702D !important;
}
.st-key-home_dashboard_link_card [data-testid="stPageLink"] a:hover,
.st-key-home_prediction_link_card [data-testid="stPageLink"] a:hover {
    filter: brightness(1.10);
    border-color: #174B2A !important;
    transform: translateY(-3px);
    box-shadow: 6px 8px 14px rgba(36,93,43,.28);
}
</style>
<div class="hero-panel">
  <div class="hero-title">Food Waste Analysis</div>
  <p class="hero-subtitle">A clear view of food distribution, demand patterns and wastage prediction.</p>
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
    <div class="metric-description" aria-label="Platform description"></div>
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
        background: linear-gradient(145deg, #FFFCF6, #F0E5D4);
        border: 1.5px solid #B9A184;
        box-shadow: 7px 7px 16px rgba(90,68,52,.14), -6px -6px 14px rgba(255,255,255,.88);
        transition: transform .28s ease, box-shadow .28s ease, border-color .28s ease;
        backdrop-filter: blur(22px) saturate(155%);
        opacity: 0;
        transform: translateX(-28px) scale(.97);
      }}
      .stat-card:hover {{
        transform: translateY(-7px) scale(1.015) !important;
        border-color: #80674F;
        box-shadow: 12px 16px 24px rgba(90,68,52,.20), -5px -5px 14px rgba(255,255,255,.9);
      }}
      .stat-card.is-visible {{
        animation: statSlideIn .48s cubic-bezier(.2,.75,.25,1) forwards;
      }}
      @keyframes statSlideIn {{
        from {{ opacity: 0; transform: translateX(-28px) scale(.97); }}
        to {{ opacity: 1; transform: translateX(0) scale(1); }}
      }}
      .stat-label {{ color: #877967; font-size: .92rem; font-weight: 650; margin-bottom: 8px; }}
      .stat-number {{ color: #2EA334; font-size: 2.15rem; font-weight: 750; line-height: 1.1; font-variant-numeric: tabular-nums; }}
      .metric-description {{
        display: none;
        margin-top: 17px;
        color: #786B5B;
        font-size: 20px;
        line-height: 1.55;
        min-height: 64px;
        letter-spacing: .12px;
        max-width: 1120px;
      }}
      .metric-description::after {{
        content: "";
        display: inline-block;
        width: 2px;
        height: 1em;
        margin-left: 4px;
        vertical-align: -2px;
        background: #2EA334;
        animation: typingCaret .8s steps(1) infinite;
      }}
      @keyframes typingCaret {{ 50% {{ opacity: 0; }} }}
      @media (min-width: 701px) {{
        .metric-description {{ display: block; }}
      }}
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
      const cards = Array.from(document.querySelectorAll(".stat-card"));
      const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      const description = document.querySelector(".metric-description");
      const descriptionText = "Explore food distribution across states, districts and blocks, then use our two-stage machine-learning model to estimate food wastage and the remaining usable quantity.";
      if (description && window.matchMedia("(min-width: 701px)").matches) {{
        if (reduced) {{
          description.textContent = descriptionText;
        }} else {{
          let charIndex = 0;
          const typeNext = () => {{
            if (charIndex < descriptionText.length) {{
              description.textContent += descriptionText.charAt(charIndex++);
              window.setTimeout(typeNext, 18);
            }}
          }};
          window.setTimeout(typeNext, 450);
        }}
      }}
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
    st.components.v1.html(metrics_html, height=225, scrolling=False)
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

