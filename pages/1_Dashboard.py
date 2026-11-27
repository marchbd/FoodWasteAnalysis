import re
import streamlit as st
import streamlit.components.v1 as components
from utils.data_loader import load_dataset
from utils.theme import apply_theme
from utils.navigation import render_top_nav

apply_theme()
render_top_nav("dashboard")

st.title("Food Waste Dashboard")
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
<div class="metric-description" aria-label="Dashboard description"></div>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; font-family: sans-serif; background: transparent; }}
  .metrics-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; }}
  .metric-card {{
    min-height: 140px; padding: 25px 24px;
    opacity: 0;
    transform: translateX(-34px) scale(.97);
    position: relative;
    border: 1px solid #8FB29A;
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(65,53,36,.08), inset 0 1px 0 rgba(255,255,255,.9);
    transition: transform .24s ease, box-shadow .24s ease, border-color .24s ease;
    background: linear-gradient(145deg, #FFFFFF, #E5F3E6);
    display: flex; flex-direction: column; justify-content: center;
  }}
  .metric-card:hover {{
    transform: translateY(-5px) scale(1.012) !important;
    border-color: #B4D92E;
    box-shadow: 0 14px 26px rgba(8,127,91,.22), inset 0 1px 0 rgba(255,255,255,.9);
  }}
  .metric-card.is-visible {{
    animation: cardSlideIn .58s cubic-bezier(.2,.75,.25,1) forwards;
  }}
  @keyframes cardSlideIn {{
    from {{ opacity: 0; transform: translateX(-34px) scale(.97); }}
    to {{ opacity: 1; transform: translateX(0) scale(1); }}
  }}
  .card-cyan {{ border-color: #78C99A; background: linear-gradient(145deg, #E3F8E9, #BFEBD0); }}
  .card-blue {{ border-color: #83BCEB; background: linear-gradient(145deg, #E5F2FF, #C9E4FA); }}
  .card-pink {{ border-color: #F3A47E; background: linear-gradient(145deg, #FFF0E8, #FFD8C5); }}
  .card-violet {{ border-color: #D6C64A; background: linear-gradient(145deg, #FBF9D9, #F1ECA9); }}
  .metric-label {{ color: #40594B; font-size: 16px; font-weight: 650; margin-bottom: 12px; }}
  .metric-value {{ color: #173D2E; font-size: clamp(30px, 3.2vw, 42px); line-height: 1.1; font-weight: 800; font-variant-numeric: tabular-nums; }}
  .metric-description {{
    display: none;
    margin-top: 18px;
    color: #263F33;
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
    background:  #087F5B;
    animation: typingCaret .8s steps(1) infinite;
  }}
  @keyframes typingCaret {{ 50% {{ opacity: 0; }} }}
  @media (min-width: 701px) {{
    .metric-description {{ display: block; }}
  }}
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
  const description = document.querySelector(".metric-description");
  const descriptionText = "Compare state-wise records, districts and blocks through the coverage table and chart to understand the geographic distribution of the dataset.";
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
components.html(metric_html, height=245, scrolling=False)


st.subheader("Geographic coverage")
coverage = (
    data[data["block"].astype(str).str.upper() != "UNKNOWN"]
    .groupby("state", as_index=False)
    .agg(districts=("district", "nunique"), blocks=("block", "nunique"), records=("state", "size"))
    .sort_values("state")
)
coverage_html = coverage.to_html(index=False, border=0, classes="coverage-table")

# Stagger each body row vertically by 0.05 seconds.
row_index = 0
def stagger_coverage_rows(match):
    global row_index
    body = match.group(1)
    def add_row_delay(_):
        global row_index
        current_row = row_index
        row_index += 1
        return f'<tr style="--row-index: {current_row}; --row-delay: {current_row * 0.36:.2f}s;">'
    body = re.sub(r"<tr>", add_row_delay, body)
    return f"<tbody>{body}</tbody>"

coverage_html = re.sub(
    r"<tbody>(.*?)</tbody>",
    stagger_coverage_rows,
    coverage_html,
    flags=re.DOTALL,
)
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
    border-spacing: 0; color: #383229; font-size: 16px;
    background: #FBF7F0; border-radius: 14px;
    overflow: hidden;
  }}
  .coverage-table th, .coverage-table td {{
    padding: 13px 16px; text-align: left;
    border-bottom: 1px solid #D8CBB7;
    white-space: nowrap;
  }}
  .coverage-table th {{
    color: #172B25; font-weight: 800;
    background: linear-gradient(110deg, #DDF7E8, #BDECCB);
  }}
  .coverage-table tbody tr:last-child td {{ border-bottom: 0; }}
  .coverage-table tbody tr:hover td {{ background: rgba(8,127,91,.12); }}
  @keyframes coverageHeadingIn {{
    from {{ opacity: 0; transform: translateX(-26px); }}
    to {{ opacity: 1; transform: translateX(0); }}
  }}
  @keyframes coverageCellIn {{
    from {{ opacity: 0; transform: translateY(-16px) translateX(-10px) scale(.97); }}
    to {{ opacity: 1; transform: translateY(0) translateX(0) scale(1); }}
  }}
  .coverage-table thead th {{
    opacity: 0;
    animation: coverageHeadingIn .55s cubic-bezier(.2,.75,.25,1) forwards;
  }}
  /* Slower diagonal wave: rows move downward while each column trails the previous one. */
  .coverage-table thead th:nth-child(1) {{ animation-delay: 0s; }}
  .coverage-table thead th:nth-child(2) {{ animation-delay: .55s; }}
  .coverage-table thead th:nth-child(3) {{ animation-delay: 1.1s; }}
  .coverage-table thead th:nth-child(4) {{ animation-delay: 1.65s; }}
  .coverage-table tbody td {{
    opacity: 0;
    animation: coverageCellIn .55s cubic-bezier(.2,.75,.25,1) forwards;
  }}
  .coverage-table tbody td:nth-child(1) {{ animation-delay: calc(.35s + var(--row-delay)); }}
  .coverage-table tbody td:nth-child(2) {{ animation-delay: calc(.9s + var(--row-delay)); }}
  .coverage-table tbody td:nth-child(3) {{ animation-delay: calc(1.45s + var(--row-delay)); }}
  .coverage-table tbody td:nth-child(4) {{ animation-delay: calc(2s + var(--row-delay)); }}
  @media (prefers-reduced-motion: reduce) {{
    .coverage-table thead th, .coverage-table tbody td {{
      opacity: 1; animation: none;
    }}
  }}
</style>
"""
components.html(coverage_component, height=coverage_height, scrolling=False)

st.subheader("Records by state")
state_counts = data.groupby("state").size().sort_values(ascending=False)
st.bar_chart(state_counts)

