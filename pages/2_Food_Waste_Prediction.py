import streamlit as st
import plotly.graph_objects as go
import uuid
from datetime import datetime
from prediction.pipeline import models_ready, predict_food_waste
from utils.data_loader import load_dataset
from utils.theme import apply_theme
from utils.navigation import render_top_nav

apply_theme()
render_top_nav("prediction")

st.markdown("""<style>
.prediction-kicker { color:#A65B49; font-size:.78rem; letter-spacing:.16em; font-weight:800; margin:4px 0 10px; }
.st-key-location_period_card, .st-key-demand_stock_card {
    border:1px solid #D8D6C8 !important;
    border-radius:15px !important;
    padding:1rem 1.1rem .75rem !important;
    background:#FBFAF5 !important;
    box-shadow:0 2px 7px rgba(37,54,44,.045) !important;
    transition:box-shadow .2s ease, border-color .2s ease;
}
.st-key-location_period_card:hover, .st-key-demand_stock_card:hover {
    border-color:#B8B5A7 !important;
    box-shadow:0 5px 14px rgba(37,54,44,.07) !important;
}
.st-key-location_period_card h3, .st-key-demand_stock_card h3 {
    color:#203A30 !important;
    font-family:Georgia, "Times New Roman", serif !important;
    font-size:1.2rem !important;
    font-weight:700 !important;
}
.st-key-location_period_card label, .st-key-demand_stock_card label {
    color:#56645B !important;
    font-weight:600 !important;
}
.st-key-location_period_card div[data-baseweb='select'] > div,
.st-key-location_period_card div[data-baseweb='input'] > div,
.st-key-demand_stock_card div[data-baseweb='input'] > div {
    border:1px solid #D2D0C3 !important;
    background:#FFFDF8 !important;
}
.st-key-location_period_card [data-testid="stHorizontalBlock"] {
    flex-wrap:nowrap !important;
}
.st-key-location_period_card [data-testid="column"] {
    min-width:0 !important;
}
[data-testid="stMetric"] {
    border:1px solid #D8D6C8 !important;
    border-radius:14px !important;
    background:#FBFAF5 !important;
}
[data-testid="stMetricValue"] {
    color:#204F3E !important;
    font-family:Georgia,serif !important;
}
@media (max-width:700px) {
    .st-key-location_period_card, .st-key-demand_stock_card { padding:.8rem !important; }
    .st-key-location_period_card [data-testid="stHorizontalBlock"],
    .st-key-demand_stock_card [data-testid="stHorizontalBlock"] {
        flex-wrap:nowrap !important;
        gap:.5rem !important;
    }
    .st-key-location_period_card [data-testid="column"],
    .st-key-demand_stock_card [data-testid="column"] {
        min-width:0 !important;
        width:50% !important;
        flex:1 1 50% !important;
    }
    .st-key-location_period_card label,
    .st-key-demand_stock_card label { font-size:.78rem !important; }
    .st-key-location_period_card input,
    .st-key-demand_stock_card input { font-size:.85rem !important; }
}
</style>""", unsafe_allow_html=True)

st.markdown('<div class="prediction-kicker">STAGE 1 → STAGE 2</div>', unsafe_allow_html=True)
st.title("Food waste prediction")
st.caption("Distribution is predicted first, then food wastage.")

data = load_dataset()
if data is None:
    st.error("Dataset is missing. Add data/raw/Datasetfood.csv to the GitHub repository.")
    st.stop()

# Dropdown choices are derived only from records present in the dataset.
for col in ("state", "district", "block", "commodity"):
    if col not in data.columns:
        st.error(f"The dataset is missing the required column: {col}")
        st.stop()

states = sorted(data["state"].dropna().astype(str).unique().tolist())
if not states:
    st.error("No states are available in the dataset.")
    st.stop()

if not models_ready():
    st.warning("Trained models are not available. Ensure both .cbm files are committed under models/.")

with st.container(border=True, key="location_period_card"):
    st.subheader("Location and period")
    location_col, period_col = st.columns([1, 1])
    with location_col:
        state = st.selectbox("State", states, key="prediction_state")
    with period_col:
        prediction_month = st.text_input("Month (YYYY-MM)", value="2026-11")

    state_data = data[data["state"].astype(str) == state]
    districts = sorted(state_data["district"].dropna().astype(str).unique().tolist())
    if not districts:
        st.error("No district data is available for this state.")
        st.stop()
    # State-specific keys ensure the district selection resets to a valid
    # option whenever the selected state changes.
    district = st.selectbox(
        "District", districts, key=f"prediction_district_{state}"
    )
    district_data = state_data[state_data["district"].astype(str) == district]
    available_blocks = sorted(
        b for b in district_data["block"].dropna().astype(str).unique().tolist()
        if b.strip() and b.upper() != "UNKNOWN"
    )
    block_choice = st.selectbox(
        "Block (optional)",
        ["Skip block (optional)"] + available_blocks,
        key=f"prediction_block_{state}_{district}",
    )
    block = "" if block_choice == "Skip block (optional)" else block_choice
    commodities = sorted(district_data["commodity"].dropna().astype(str).unique().tolist())
    if not commodities:
        st.error("No commodity data is available for this district.")
        st.stop()
    commodity = st.selectbox(
        "Commodity", commodities, key=f"prediction_commodity_{state}_{district}"
    )

st.write("")
with st.form("prediction_inputs"):
    with st.container(border=True, key="demand_stock_card"):
        st.subheader("Demand and stock")
        demand_col, stock_col = st.columns(2)
        with demand_col:
            beneficiaries = st.number_input("Expected beneficiaries", min_value=1, value=500, step=1)
            transactions = st.number_input("Expected transactions", min_value=1, value=400, step=1)
            previous_wastage = st.number_input("Previous month's wastage (kg)", min_value=0.0, value=25.0, step=1.0)
            storage_days = st.number_input("Expected storage duration (days)", min_value=1, max_value=90, value=25, step=1)
        with stock_col:
            opening_stock = st.number_input("Opening stock (kg)", min_value=0.0, value=600.0, step=10.0)
            received_stock = st.number_input("Expected received stock (kg)", min_value=0.0, value=2500.0, step=10.0)
            storage_capacity = st.number_input("Storage capacity (kg)", min_value=1.0, value=3000.0, step=10.0)
            delivery_delay = st.number_input("Expected delivery delay (days)", min_value=0, max_value=60, value=7, step=1)

    submitted = st.form_submit_button(
        "Predict distribution and wastage",
        type="primary",
        use_container_width=True,
        disabled=not models_ready(),
    )
if submitted:
    try:
        result = predict_food_waste({
            "state": state,
            "district": district,
            "block": block,
            "commodity": commodity,
            "prediction_month": prediction_month.strip(),
            "opening_stock_kg": opening_stock,
            "received_stock_kg": received_stock,
            "beneficiaries": beneficiaries,
            "transactions": transactions,
            "storage_capacity_kg": storage_capacity,
            "storage_days": storage_days,
            "delivery_delay_days": delivery_delay,
            "previous_wastage_kg": previous_wastage,
        })
        st.markdown(
            '<div id="prediction-results-anchor" style="scroll-margin-top: 0;"></div>',
            unsafe_allow_html=True,
        )
        scroll_trigger = uuid.uuid4().hex
        scroll_html = """
            <script>
              // This component is uniquely refreshed for every Predict submission.
              window.setTimeout(() => {
                try {
                  const doc = window.parent.document;
                  const target = doc.getElementById("prediction-results-anchor");
                  if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
                } catch (error) {
                  console.warn("Could not scroll to prediction results:", error);
                }
              }, 400);
            </script>
            <!-- scroll-trigger: """ + scroll_trigger + """ -->
        """
        st.components.v1.html(scroll_html, height=1, scrolling=False)
        st.subheader("Prediction results")
        m1, m2 = st.columns(2)
        m1.metric("Predicted distributed quantity", f"{result['predicted_distributed_stock_kg']:,.2f} kg")
        m2.metric("Predicted food wastage", f"{result['predicted_wastage_kg']:,.2f} kg")

        distributed = max(0.0, float(result["predicted_distributed_stock_kg"]))
        wastage = max(0.0, float(result["predicted_wastage_kg"]))

        # Forecast the submitted month and the following two months.
        current_period = datetime.strptime(prediction_month.strip(), "%Y-%m")
        forecast_points = []
        for offset in range(3):
            month_index = current_period.month - 1 + offset
            forecast_year = current_period.year + month_index // 12
            forecast_month_number = month_index % 12 + 1
            forecast_date = datetime(forecast_year, forecast_month_number, 1)
            forecast_month = forecast_date.strftime("%Y-%m")
            if offset == 0:
                forecast_distribution = distributed
                forecast_wastage = wastage
            else:
                forecast_inputs = {
                    "state": state,
                    "district": district,
                    "block": block,
                    "commodity": commodity,
                    "prediction_month": forecast_month,
                    "opening_stock_kg": opening_stock,
                    "received_stock_kg": received_stock,
                    "beneficiaries": beneficiaries,
                    "transactions": transactions,
                    "storage_capacity_kg": storage_capacity,
                    "storage_days": storage_days,
                    "delivery_delay_days": delivery_delay,
                    "previous_wastage_kg": previous_wastage,
                }
                forecast_result = predict_food_waste(forecast_inputs)
                forecast_distribution = max(0.0, float(forecast_result["predicted_distributed_stock_kg"]))
                forecast_wastage = max(0.0, float(forecast_result["predicted_wastage_kg"]))

            risk = (forecast_wastage / forecast_distribution * 100) if forecast_distribution > 0 else None
            forecast_points.append({
                "month": forecast_date.strftime("%B"),
                "year": forecast_year,
                "risk": risk,
            })

        current_risk = forecast_points[0]["risk"]
        st.subheader("Distribution breakdown")
        chart_col, risk_col = st.columns([1.55, 1], gap="medium")

        with chart_col:
            if distributed <= 0:
                st.info("A doughnut breakdown is unavailable because the predicted distributed quantity is zero.")
            elif wastage > distributed:
                st.warning(
                    "Predicted wastage is higher than predicted distributed quantity, "
                    "so a distribution breakdown would be misleading. Please review the inputs."
                )
            else:
                usable = distributed - wastage
                wastage_pct = current_risk
                circumference = 2 * 3.141592653589793 * 108
                usable_arc = circumference * (usable / distributed)
                wastage_arc = circumference * (wastage / distributed)
                wastage_start_angle = 360 * (usable / distributed)
                donut_html = f"""
                <div class="donut-wrap">
                  <svg class="donut-svg" viewBox="0 0 300 300" role="img" aria-label="Usable quantity {usable:,.2f} kilograms and predicted wastage {wastage:,.2f} kilograms">
                    <circle cx="150" cy="150" r="108" fill="none" stroke="rgba(148,163,184,.13)" stroke-width="46"/>
                    <circle cx="150" cy="150" r="108" fill="none" stroke="#204F3E" stroke-width="46"
                            stroke-linecap="butt" transform="rotate(-90 150 150)"
                            stroke-dasharray="0 {circumference:.3f}">
                      <animate attributeName="stroke-dasharray" from="0 {circumference:.3f}" to="{usable_arc:.3f} {circumference:.3f}" dur="1.1s" fill="freeze"/>
                    </circle>
                    <circle cx="150" cy="150" r="108" fill="none" stroke="#B85F4C" stroke-width="46"
                            stroke-linecap="butt" transform="rotate({wastage_start_angle - 90:.3f} 150 150)"
                            stroke-dasharray="0 {circumference:.3f}">
                      <animate attributeName="stroke-dasharray" from="0 {circumference:.3f}" to="{wastage_arc:.3f} {circumference:.3f}" begin=".12s" dur="1.1s" fill="freeze"/>
                    </circle>
                    <text x="150" y="146" text-anchor="middle" fill="#203A30" font-size="22" font-weight="600">{wastage_pct:.1f}%</text>
                    <text x="150" y="169" text-anchor="middle" fill="#68746B" font-size="14">wasted</text>
                  </svg>
                  <div class="donut-legend">
                    <span><i class="usable-dot"></i>Usable quantity</span>
                    <span><i class="waste-dot"></i>Predicted wastage</span>
                  </div>
                </div>
                <style>
                  .donut-wrap {{ width:100%; display:flex; flex-direction:column; align-items:center; color:#203A30; }}
                  .donut-svg {{ width:min(100%, 330px); height:auto; overflow:visible; }}
                  .donut-legend {{ display:flex; justify-content:center; flex-wrap:wrap; gap:12px; margin-top:0; font:600 13px sans-serif; }}
                  .donut-legend span {{ display:flex; align-items:center; gap:7px; }}
                  .donut-legend i {{ width:12px; height:12px; display:inline-block; }}
                  .usable-dot {{ background:#204F3E; }}
                  .waste-dot {{ background:#B85F4C; }}
                  @media (prefers-reduced-motion: reduce) {{ .donut-svg animate {{ display:none; }} }}
                </style>
                """
                st.components.v1.html(donut_html, height=350, scrolling=False)
                usable_col, wastage_col = st.columns(2)
                usable_col.metric("Usable quantity", f"{usable:,.2f} kg")
                wastage_col.metric("Wastage share", f"{wastage_pct:.1f}%")

        with risk_col:
            valid_risks = [point["risk"] for point in forecast_points if point["risk"] is not None]
            if not valid_risks:
                st.info("Risk factors cannot be calculated because predicted distribution is zero for all three months.")
            else:
                max_risk = max(valid_risks)
                chart_top = max(10, int((max_risk * 1.2 + 4) // 5) * 5)
                # Five evenly spaced Y-axis ticks, matching the five grid lines.
                tick_values = [round(chart_top * index / 4) for index in range(4, -1, -1)]
                tick_labels = "".join(
                    f'<div class="risk-y-tick">{tick}%</div>'
                    for tick in tick_values
                )
                bars = []
                bar_colors = ["#B85F4C", "#204F3E", "#6F9B83"]
                for index, point in enumerate(forecast_points):
                    risk = point["risk"]
                    bar_height = max(2.0, (risk / chart_top) * 220) if risk is not None else 2.0
                    value_label = f"{risk:.1f}%" if risk is not None else "N/A"
                    bars.append(
                        f'<div class="risk-bar-column">'
                        f'<div class="risk-value-label" style="--bar-height:{bar_height:.1f}px">{value_label}</div>'
                        f'<div class="risk-bar" style="--bar-height:{bar_height:.1f}px;--bar-color:{bar_colors[index]};--bar-delay:{index * 0.22:.2f}s"></div>'
                        f'</div>'
                    )
                month_labels = "".join(
                    f'<div class="risk-month">{point["month"]}<span>{point["year"]}</span></div>'
                    for point in forecast_points
                )
                risk_aria_label = ", ".join(
                    f"{point['month']} {point['year']}: {point['risk']:.1f}%"
                    if point["risk"] is not None
                    else f"{point['month']} {point['year']}: unavailable"
                    for point in forecast_points
                )
                risk_chart_html = f"""
                <div class="risk-chart-card">
                  <div class="risk-chart-title">Wastage risk forecast</div>
                  <div class="risk-chart-subtitle">Current month and next two months</div>
                  <div class="risk-chart" role="img" aria-label="Predicted wastage risk: {risk_aria_label}">
                    <div class="risk-y-axis"><div class="risk-y-title">Risk (%)</div>{tick_labels}</div>
                    <div class="risk-plot">
                      <div class="risk-grid-lines"><i></i><i></i><i></i><i></i><i></i></div>
                      <div class="risk-bars">{''.join(bars)}</div>
                      <div class="risk-months">{month_labels}</div>
                      <div class="risk-x-title">Month</div>
                    </div>
                  </div>
                </div>
                <style>
                  .risk-chart-card {{ background:#FBFAF5; border:1px solid #D8D6C8; border-radius:15px; padding:19px 16px 17px; box-shadow:0 2px 7px rgba(37,54,44,.045); }}
                  .risk-chart-title {{ color:#203A30; font:700 1.45rem Georgia,serif; }}
                  .risk-chart-subtitle {{ color:#46584E; font:1rem sans-serif; margin-top:6px; }}
                  .risk-chart {{ display:flex; gap:10px; margin-top:17px; }}
                  .risk-y-axis {{ width:46px; flex:0 0 46px; height:320px; display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end; padding:0 4px 76px 0; position:relative; box-sizing:border-box; }}
                  .risk-y-title {{ position:absolute; top:42%; left:-9px; transform:translate(-100%,-50%) rotate(-90deg); transform-origin:right center; color:#263A32; font:700 .85rem sans-serif; white-space:nowrap; }}
                  .risk-y-tick {{ color:#263A32; font:600 .88rem sans-serif; line-height:1; transform:translateY(50%); }}
                  .risk-plot {{ position:relative; flex:1; min-width:0; height:320px; border-left:2px solid #526258; box-sizing:border-box; }}
                  .risk-grid-lines {{ position:absolute; inset:0 0 76px 0; display:flex; flex-direction:column; justify-content:space-between; pointer-events:none; }}
                  .risk-grid-lines i {{ display:block; border-top:1px solid #D5D7CC; width:100%; }}
                  .risk-grid-lines i:last-child {{ border-top:2px solid #526258; }}
                  .risk-bars {{ position:absolute; inset:0 0 76px 0; display:flex; justify-content:space-around; gap:9px; }}
                  .risk-bar-column {{ flex:1; min-width:0; height:100%; display:flex; flex-direction:column; justify-content:flex-end; align-items:center; position:relative; }}
                  .risk-value-label {{ position:absolute; bottom:calc(var(--bar-height) + 7px); width:100%; text-align:center; color:#203A30; font:700 1.05rem Georgia,serif; white-space:nowrap; }}
                  .risk-bar {{ display:block; flex:none; height:var(--bar-height); width:min(72%,66px); background:var(--bar-color); border-radius:7px 7px 0 0; transform:scaleY(0); transform-origin:bottom; animation:riskBarRise .9s cubic-bezier(.2,.75,.25,1) var(--bar-delay) forwards; box-shadow:0 3px 8px rgba(32,58,48,.12); z-index:1; }}
                  @keyframes riskBarRise {{ from {{ transform:scaleY(0); }} to {{ transform:scaleY(1); }} }}
                  .risk-months {{ position:absolute; left:0; right:0; bottom:29px; height:42px; display:flex; gap:9px; }}
                  .risk-month {{ flex:1; min-width:0; color:#203A30; font:700 .98rem sans-serif; text-align:center; white-space:nowrap; }}
                  .risk-month span {{ display:block; color:#46584E; font-size:.86rem; font-weight:500; margin-top:3px; }}
                  .risk-x-title {{ position:absolute; bottom:4px; left:0; right:0; text-align:center; color:#263A32; font:700 .85rem sans-serif; }}
                  @media (max-width:700px) {{
                    .risk-chart-card {{ padding:16px 10px 14px; }}
                    .risk-chart-title {{ font-size:1.25rem; }}
                    .risk-chart-subtitle {{ font-size:.9rem; }}
                    .risk-chart {{ gap:5px; }}
                    .risk-y-axis {{ width:39px; flex-basis:39px; }}
                    .risk-y-tick {{ font-size:.78rem; }}
                    .risk-value-label {{ font-size:.9rem; }}
                    .risk-month {{ font-size:.83rem; }}
                    .risk-month span {{ font-size:.75rem; }}
                  }}
                  @media (prefers-reduced-motion: reduce) {{ .risk-bar {{ animation:none; transform:scaleY(1); }} }}
                </style>
                """
                st.components.v1.html(risk_chart_html, height=390, scrolling=False)

        if distributed > 0 and wastage <= distributed:
            with st.expander("See How?"):
                st.latex(r"\text{Usable quantity (kg)} = \text{Predicted distribution (kg)} - \text{Predicted wastage (kg)}")
                st.latex(r"\text{Wastage share (\%)} = \frac{\text{Predicted wastage (kg)}}{\text{Predicted distribution (kg)}} \times 100")

    except Exception as exc:
        st.error(f"Could not generate prediction: {exc}")
