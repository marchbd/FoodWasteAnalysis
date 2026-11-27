import streamlit as st

from utils.data_loader import load_dataset
from utils.theme import apply_theme
from utils.navigation import render_top_nav

st.set_page_config(page_title="Food Waste Analysis", page_icon="🍚", layout="wide")
apply_theme()
render_top_nav("home")

st.markdown("""
<style>
.block-container { padding-top: 2.8rem !important; }
.hero-panel {
    position: relative; overflow: hidden; isolation: isolate;
    box-sizing: border-box; width: 100%;
    padding: clamp(28px, 4vw, 46px);
    border-radius: 18px;
    background: #F4F2E9;
    border: 1px solid #D8D6C8;
    box-shadow: none;
    margin: 8px 0 24px;
}
.hero-panel:before {
    content:""; position:absolute; z-index:-1; width:290px; height:290px;
    right:-90px; bottom:-180px; border-radius:50%;
    background:radial-gradient(circle, rgba(56,157,190,.34), transparent 68%);
}
.hero-panel:after {
    content:""; position:absolute; z-index:-1; width:190px; height:190px;
    right:14%; top:-130px; border-radius:50%;
    background:radial-gradient(circle, rgba(229,107,85,.34), transparent 70%);
    animation: heroFloat 8s ease-in-out infinite alternate;
}
.hero-kicker { color:#A65B49; font-size:.82rem; letter-spacing:.16em; font-weight:800; margin:0 0 16px; }
.hero-title {
    color:#203A30; font-family:Georgia, "Times New Roman", serif;
    font-size:clamp(2.15rem,4.5vw,3.5rem);
    font-weight:700; letter-spacing:-.035em; line-height:1.06; margin:0 0 12px;
}
.hero-subtitle { color:#56645B; font-size:clamp(1.05rem,1.5vw,1.2rem); line-height:1.6; margin:0 0 22px; max-width:760px; }
.stage-row { display:flex; flex-wrap:wrap; gap:10px; align-items:center; }
.stage-pill {
    display:inline-flex; align-items:center; padding:9px 15px; border-radius:999px;
    color:#204F3E; background:#FBFAF5;
    border:1px solid #D8D6C8; font-size:.92rem; font-weight:700;
    box-shadow:0 3px 10px rgba(41,37,31,.05);
}
 .stage-arrow { color:#B85F4C; font-size:1.25rem; font-weight:800; }
.dataset-note { color:#69756C; font-size:.9rem; margin-top:10px; }
@keyframes heroFloat { from { transform:translate3d(0,0,0); } to { transform:translate3d(-18px,16px,0); } }
.st-key-home_dashboard_link_card, .st-key-home_prediction_link_card {
    background:#FBFAF5 !important;
    border:1px solid #D8D6C8 !important; border-radius:16px !important;
    box-shadow:0 2px 7px rgba(37,54,44,.045) !important;
    transition:transform .24s ease, box-shadow .24s ease, border-color .24s ease;
    padding:18px 20px !important;
}
.st-key-home_dashboard_link_card:hover, .st-key-home_prediction_link_card:hover {
    transform:translateY(-5px);
    border-color:#B8B5A7 !important;
    box-shadow:0 15px 28px rgba(36,107,69,.14) !important;
}
.st-key-home_dashboard_link_card [data-testid="stPageLink"] a,
.st-key-home_prediction_link_card [data-testid="stPageLink"] a {
    display:flex !important; align-items:center !important; justify-content:center !important;
    min-height:48px; padding:10px 16px !important; border-radius:12px !important;
    color:#fff !important; -webkit-text-fill-color:#fff !important;
    font-weight:750 !important; text-decoration:none !important;
    transition:transform .2s ease, filter .2s ease, box-shadow .2s ease;
}
.st-key-home_dashboard_link_card [data-testid="stPageLink"] a {
    background:#204F3E !important;
    border:1px solid #173F32 !important; box-shadow:none;
}
.st-key-home_prediction_link_card [data-testid="stPageLink"] a {
    background:#204F3E !important;
    border:1px solid #173F32 !important; box-shadow:none;
}
.st-key-home_dashboard_link_card [data-testid="stPageLink"] a:hover,
.st-key-home_prediction_link_card [data-testid="stPageLink"] a:hover {
    transform:translateY(-2px); filter:brightness(1.08);
    box-shadow:0 5px 12px rgba(32,79,62,.18);
}
@media (max-width:700px) {
  .block-container { padding-top:.55rem !important; }
  .hero-panel { padding:22px 2px 16px; margin:0 0 14px; border:0; border-radius:0; background:transparent; }
  .hero-kicker { font-size:.76rem; margin-bottom:14px; }
  .hero-title { font-size:clamp(2.05rem,8vw,2.55rem); line-height:1.08; margin-bottom:12px; }
  .hero-subtitle { font-size:1.02rem; line-height:1.5; margin-bottom:20px; }
  .stage-row { gap:7px; }
  .stage-pill { padding:8px 12px; font-size:.82rem; }
   .dataset-note { display:none; }
  .stats-grid { gap:0 !important; border:1px solid #D8D6C8; border-radius:13px; overflow:hidden; }
  .stat-card { border:0 !important; border-radius:0; box-shadow:none; min-height:108px; padding:16px; background:#FBFAF5 !important; }
  .stat-card:nth-child(odd) { border-right:1px solid #D8D6C8 !important; }
  .stat-card:nth-child(-n+2) { border-bottom:1px solid #D8D6C8 !important; }
  .stat-card:hover { transform:none !important; box-shadow:none !important; }
  .stat-label { font-size:.78rem; letter-spacing:.1em; text-transform:uppercase; }
  .stat-number { font-size:2rem; }
  .st-key-home_dashboard_link_card, .st-key-home_prediction_link_card { margin-top:14px; }
}
@media (prefers-reduced-motion: reduce) { .hero-panel:after { animation:none; } }
</style>
<div class="hero-panel">
  <div class="hero-kicker">TWO-STAGE MACHINE LEARNING</div>
  <div class="hero-title">Know how much food will be wasted, before it is.</div>
  <p class="hero-subtitle">Estimate food distribution across states, districts and blocks, then predict wastage and the usable quantity that remains.</p>
  <div class="stage-row">
    <span class="stage-pill">1 · Distribution</span>
    <span class="stage-arrow">→</span>
    <span class="stage-pill">2 · Wastage</span>
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
        background: #FBFAF5;
        border: 1px solid #D8D6C8;
        box-shadow: 7px 7px 16px rgba(90,68,52,.14), -6px -6px 14px rgba(255,255,255,.88);
        transition: transform .28s ease, box-shadow .28s ease, border-color .28s ease;
        backdrop-filter: blur(22px) saturate(155%);
        opacity: 0;
        transform: translateX(-28px) scale(.97);
      }}
      .stat-card:nth-child(1), .stat-card:nth-child(2), .stat-card:nth-child(3), .stat-card:nth-child(4) {{ background:#FBFAF5; border-color:#D8D6C8; }}
      .stat-card .stat-number {{ color:#204F3E; font-family:Georgia,serif; }}
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
      .stat-label {{ color: #69756C; font-size: 1rem; font-weight: 700; margin-bottom: 8px; }}
      .stat-number {{ color: #087F8C; font-size: 2.2rem; font-weight: 750; line-height: 1.1; font-variant-numeric: tabular-nums; }}
      .metric-description {{
        display: none;
        margin-top: 17px;
        color: #46506A;
        font-weight: 600;
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
        background: #B85F4C;
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
    st.markdown('<div class="dataset-note">Location dropdowns show only states, districts and blocks represented in this dataset.</div>', unsafe_allow_html=True)

st.divider()

# Keep both destinations in separate, clearly visible cards.
left, right = st.columns(2, gap="large")

with left:
    with st.container(border=True, key="home_dashboard_link_card"):
        st.subheader("Dashboard")
        st.write("Explore the dataset and its geographic coverage.")
        st.page_link(
            "pages/1_Dashboard.py",
            label="Open Dashboard",
            use_container_width=True,
        )

with right:
    with st.container(border=True, key="home_prediction_link_card"):
        st.subheader("Food Waste Prediction")
        st.write(
            "Choose a state and district with available data. "
            "Block selection is optional."
        )
        st.page_link(
            "pages/2_Food_Waste_Prediction.py",
            label="Open Prediction",
            use_container_width=True,
        )

