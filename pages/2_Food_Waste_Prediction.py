import streamlit as st
import plotly.graph_objects as go
from prediction.pipeline import models_ready, predict_food_waste
from utils.data_loader import load_dataset
from utils.theme import apply_theme

apply_theme()

st.title("🔮 Food Waste Prediction")
st.caption("Two-stage prediction: distribution first, then food wastage.")

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

with st.form("prediction_inputs"):
    st.subheader("Location and period information")
    state = st.selectbox("State", states)
    state_data = data[data["state"].astype(str) == state]
    districts = sorted(state_data["district"].dropna().astype(str).unique().tolist())
    if not districts:
        st.error("No district data is available for this state.")
        st.stop()
    district = st.selectbox("District", districts)
    district_data = state_data[state_data["district"].astype(str) == district]
    available_blocks = sorted(
        b for b in district_data["block"].dropna().astype(str).unique().tolist()
        if b.strip() and b.upper() != "UNKNOWN"
    )
    block_choice = st.selectbox("Block (optional)", ["Skip block (optional)"] + available_blocks)
    block = "" if block_choice == "Skip block (optional)" else block_choice

    commodities = sorted(district_data["commodity"].dropna().astype(str).unique().tolist())
    if not commodities:
        st.error("No commodity data is available for this district.")
        st.stop()
    commodity = st.selectbox("Commodity", commodities)
    prediction_month = st.text_input("Prediction month (YYYY-MM)", value="2026-11")

    st.subheader("Demand and stock estimates")
    c1, c2 = st.columns(2)
    with c1:
        beneficiaries = st.number_input("Expected beneficiaries", min_value=1, value=500, step=1)
        transactions = st.number_input("Expected transactions", min_value=1, value=400, step=1)
        opening_stock = st.number_input("Opening stock (kg)", min_value=0.0, value=600.0, step=10.0)
        received_stock = st.number_input("Expected received stock (kg)", min_value=0.0, value=2500.0, step=10.0)
    with c2:
        storage_capacity = st.number_input("Storage capacity (kg)", min_value=1.0, value=3000.0, step=10.0)
        previous_wastage = st.number_input("Previous month's wastage (kg)", min_value=0.0, value=25.0, step=1.0)
        storage_days = st.number_input("Expected storage duration (days)", min_value=1, max_value=90, value=25, step=1)
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
        st.subheader("Prediction results")
        m1, m2 = st.columns(2)
        m1.metric("Predicted distributed quantity", f"{result['predicted_distributed_stock_kg']:,.2f} kg")
        m2.metric("Predicted food wastage", f"{result['predicted_wastage_kg']:,.2f} kg")

        distributed = max(0.0, float(result["predicted_distributed_stock_kg"]))
        wastage = max(0.0, float(result["predicted_wastage_kg"]))
        st.subheader("Predicted distribution breakdown")
        if distributed <= 0:
            st.info("A doughnut breakdown is unavailable because the predicted distributed quantity is zero.")
        elif wastage > distributed:
            st.warning(
                "Predicted wastage is higher than predicted distributed quantity, "
                "so a distribution breakdown would be misleading. Please review the inputs."
            )
        else:
            usable = distributed - wastage
            wastage_pct = (wastage / distributed) * 100
            fig = go.Figure(
                data=[
                    go.Pie(
                        labels=["Usable quantity", "Predicted wastage"],
                        values=[usable, wastage],
                        hole=0.68,
                        sort=False,
                        direction="clockwise",
                        textinfo="none",
                        hovertemplate="%{label}<br>%{value:,.2f} kg (%{percent})<extra></extra>",
                    )
                ]
            )
            fig.update_layout(
                height=330,
                template='plotly_dark',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#eaf2ff'),
                margin=dict(t=20, b=20, l=10, r=10),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=-0.12, xanchor="center", x=0.5),
                annotations=[
                    dict(
                        text=f"{wastage_pct:.1f}%<br><sup>wasted</sup>",
                        x=0.5,
                        y=0.5,
                        font=dict(size=22),
                        showarrow=False,
                    )
                ],
            )
            st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
            usable_col, wastage_col = st.columns(2)
            usable_col.metric("Usable quantity", f"{usable:,.2f} kg")
            wastage_col.metric("Wastage share", f"{wastage_pct:.1f}%")

            with st.expander("See How?"):
                st.markdown("### How these values are calculated")
                st.markdown(
                    "The two models make separate predictions. Stage 1 predicts the "
                    "distributed quantity, then Stage 2 predicts the wastage using the "
                    "input features and Stage 1's predicted distribution."
                )

                st.markdown("**1. Usable quantity**")
                st.latex(r"\\text{Usable quantity} = \\text{Predicted distribution} - \\text{Predicted wastage}")
                st.code(
                    f"{distributed:,.2f} kg - {wastage:,.2f} kg = {usable:,.2f} kg",
                    language="text",
                )

                st.markdown("**2. Wastage share**")
                st.latex(r"\\text{Wastage share} = \\left(\\frac{\\text{Predicted wastage}}{\\text{Predicted distribution}}\\right) \\times 100")
                st.code(
                    f"({wastage:,.2f} kg / {distributed:,.2f} kg) × 100 = {wastage_pct:.2f}%",
                    language="text",
                )
                st.caption(
                    "Usable quantity means predicted distribution remaining after predicted wastage; "
                    "it is not a direct measurement of food consumed by beneficiaries."
                )

    except Exception as exc:
        st.error(f"Could not generate prediction: {exc}")

