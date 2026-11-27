import streamlit as st
import streamlit.components.v1 as components
from utils.data_loader import load_dataset
from utils.theme import apply_theme
from utils.navigation import render_top_nav

apply_theme()
render_top_nav("dashboard")

st.title("📊 Food Waste Dashboard")
st.caption("Geographic coverage and records across the dataset.")

data = load_dataset()
if data is None:
    st.error("Dataset missing. Add data/raw/Datasetfood.csv.")
    st.stop()

records_count = int(len(data))
states_count = int(data["state"].nunique())
districts_count = int(data["district"].nunique())
blocks_count = int(data.loc[data["block"].astype(str).str.upper() != "UNKNOWN", "block"].nunique())

metric_html = f"""
<div class="metrics-grid">
  <div class="metric-card card-cyan">
    <div class="metric-label">Records</div>
    <div class="metric-value" data-target="{records_count}">0</div>
  </div>
  <div class="metric-card card-blue">
    <div class="metric-label">States</div>
    <div class="metric-value" data-target="{states_count}">0</div>
  </div>
  <div class="metric-card card-pink">
    <div class="metric-label">Districts</div>
    <div class="metric-value" data-target="{districts_count}">0</div>
  </div>
  <div class="metric-card card-violet">
    <div class="metric-label">Blocks</div>
    <div class="metric-value" data-target="{blocks_count}">0</div>
  </div>
</div>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: sans-serif; background: transparent; }}
  .metrics-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; }}
  .metric-card {{
    min-height: 140px; padding: 25px 24px;
    opacity: 0;
    transform: translateX(-34px) scale(.97);
    position: relative;
    border: 1px solid rgba(148, 163, 184, .28);
    border-radius: 24px;
    background: linear-gradient(145deg, rgba(24, 42, 67, .88), rgba(15, 23, 42, .92));
    display: flex; flex-direction: column; justify-content: center;
  }}
  .metric-card.is-visible {{
    animation: cardSlideIn .58s cubic-bezier(.2,.75,.25,1) forwards;
  }}
  @keyframes cardSlideIn {{
    from {{ opacity: 0; transform: translateX(-34px) scale(.97); }}
    to {{ opacity: 1; transform: translateX(0) scale(1); }}
  }}
  .card-cyan {{ border-color: rgba(103,232,249,.38); }}
  .card-blue {{ border-color: rgba(96,165,250,.34); }}
  .card-pink {{ border-color: rgba(240,171,252,.34); }}
  .card-violet {{ border-color: rgba(196,181,253,.36); }}
  .metric-label {{ color: #c1cde1; font-size: 16px; margin-bottom: 12px; }}
  .metric-value {{ color: #dce6f7; font-size: clamp(28px, 3.2vw, 40px); line-height: 1.1; font-weight: 800; font-variant-numeric: tabular-nums; }}
  @media (max-width: 700px) {{
    .metrics-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }}
    .metric-card {{ min-height: 112px; padding: 18px; border-radius: 18px; }}
    .metric-label {{ font-size: 14px; margin-bottom: 8px; }}
  }}
  @media (prefers-reduced-motion: reduce) {{
    .metric-value {{ transition: none; }}
  }}
</style>
<script>
  const cards = Array.from(document.querySelectorAll(".metric-card"));
  const duration = 1250;
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function animateCount(element) {{
    const target = Number(element.dataset.target);
    const start = performance.now();
    function tick(now) {{
      const progress = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      element.textContent = Math.round(target * eased).toLocaleString("en-IN");
      if (progress < 1) requestAnimationFrame(tick);
    }}
    requestAnimationFrame(tick);
  }}

  if (reduced) {{
    cards.forEach((card) => {{
      card.classList.add("is-visible");
      const value = card.querySelector(".metric-value");
      value.textContent = Number(value.dataset.target).toLocaleString("en-IN");
    }});
  }} else {{
    function showCard(index) {{
      if (index >= cards.length) return;
      const card = cards[index];
      card.classList.add("is-visible");
      const value = card.querySelector(".metric-value");
      window.setTimeout(() => animateCount(value), 260);
      // Reveal the next card 2 seconds after this card appears.
      window.setTimeout(() => showCard(index + 1), 300);
    }}
    showCard(0);
  }}
</script>
"""
components.html(metric_html, height=155, scrolling=False)


st.subheader("Geographic coverage")
coverage = (
    data[data["block"].astype(str).str.upper() != "UNKNOWN"]
    .groupby("state", as_index=False)
    .agg(districts=("district", "nunique"), blocks=("block", "nunique"), records=("state", "size"))
    .sort_values("state")
)
coverage_html = coverage.to_html(index=False, border=0, classes="coverage-table")
coverage_height = max(300, 58 + len(coverage) * 43)

coverage_component = f"""
<div class="coverage-scroll">
  {coverage_html}
</div>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: transparent; font-family: sans-serif; }}
  .coverage-scroll {{ width: 100%; overflow-x: auto; border-radius: 14px; }}
  .coverage-table {{
    width: 100%; min-width: 520px; border-collapse: separate;
    border-spacing: 0; color: #dce6f7; font-size: 15px;
    background: rgba(15, 23, 42, .52); border-radius: 14px;
    overflow: hidden;
  }}
  .coverage-table th, .coverage-table td {{
    padding: 13px 16px; text-align: left;
    border-bottom: 1px solid rgba(148, 163, 184, .15);
    white-space: nowrap;
  }}
  .coverage-table th {{
    color: #b9d9f7; font-weight: 750;
    background: linear-gradient(110deg, rgba(14,165,233,.18), rgba(124,58,237,.18));
  }}
  .coverage-table tbody tr:last-child td {{ border-bottom: 0; }}
  .coverage-table tbody tr:hover td {{ background: rgba(56,189,248,.07); }}
  @keyframes coverageColumnIn {{
    from {{ opacity: 0; transform: translateX(-28px); }}
    to {{ opacity: 1; transform: translateX(0); }}
  }}
  .coverage-table th, .coverage-table td {{
    opacity: 0; animation: coverageColumnIn .48s cubic-bezier(.2,.75,.25,1) forwards;
  }}
  .coverage-table th:nth-child(1), .coverage-table td:nth-child(1) {{ animation-delay: 0s; }}
  .coverage-table th:nth-child(2), .coverage-table td:nth-child(2) {{ animation-delay: .3s; }}
  .coverage-table th:nth-child(3), .coverage-table td:nth-child(3) {{ animation-delay: .6s; }}
  .coverage-table th:nth-child(4), .coverage-table td:nth-child(4) {{ animation-delay: .9s; }}
  @media (prefers-reduced-motion: reduce) {{
    .coverage-table th, .coverage-table td {{ opacity: 1; animation: none; }}
  }}
</style>
"""
components.html(coverage_component, height=coverage_height, scrolling=False)

st.subheader("Records by state")
state_counts = data.groupby("state").size().sort_values(ascending=False)
st.bar_chart(state_counts)

