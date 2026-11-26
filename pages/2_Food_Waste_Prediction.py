import streamlit as st
from prediction.pipeline import load_metrics, models_ready, predict_food_waste
from utils.data_loader import load_dataset

st.title("🔮 Food Waste Prediction")
st.caption("Two-stage prediction: distribution first, then food wastage.")

data = load_dataset()
if data is None:
    st.error("Demo dataset is missing. Add data/raw/Datasetfood.csv to the GitHub repository.")
    st.stop()

# Dropdown choices are derived only from records present in the committed demo CSV.
for col in ("state", "district", "block", "commodity"):
    if col not in data.columns:
        st.error(f"The demo dataset is missing the required column: {col}")
        st.stop()

states = sorted(data["state"].dropna().astype(str).unique().tolist())
if not states:
    st.error("No states are available in the demo dataset.")
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
        st.caption("These are estimates from models trained on synthetic demonstration data, not measured government statistics.")
    except Exception as exc:
        st.error(f"Could not generate prediction: {exc}")

metrics = load_metrics()
if metrics:
    st.divider()
    st.subheader("Demo-model evaluation")
    st.caption(
        f"Training: {metrics['train_period'][0]} to {metrics['train_period'][1]} · "
        f"Test: {metrics['test_period'][0]} to {metrics['test_period'][1]}"
    )
    st.warning("These metrics evaluate synthetic demo data only; they do not measure real-world accuracy.")
    a, b = st.columns(2)
    a.metric("Distribution MAE", f"{metrics['stage1_distribution']['mae']:,.2f} kg")
    b.metric("Wastage MAE", f"{metrics['stage2_wastage']['mae']:,.2f} kg")
    with st.expander("View full metrics"):
        st.json({
            "Stage 1 — Distribution": metrics["stage1_distribution"],
            "Stage 2 — Wastage": metrics["stage2_wastage"],
            "Test rows": metrics["test_rows"],
            "Stage 2 OOF training rows": metrics["stage2_oof_train_rows"],
        })
