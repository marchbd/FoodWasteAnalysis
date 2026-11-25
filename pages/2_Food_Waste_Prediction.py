import streamlit as st
from prediction.pipeline import load_metrics, models_ready, predict_food_waste

st.title("🔮 Food Waste Prediction")
st.caption("Two-stage prediction: distribution first, then food wastage.")

if not models_ready():
    st.warning("Trained models are not available. Ensure both .cbm files are committed under models/.")

with st.form("prediction_inputs"):
    st.subheader("Location and period information")
    c1, c2 = st.columns(2)
    with c1:
        state = st.text_input("State", placeholder="e.g. West Bengal")
        district = st.text_input("District", placeholder="e.g. Murshidabad")
        block = st.text_input("Block (optional)", placeholder="Leave blank if unknown")
    with c2:
        commodity = st.selectbox("Commodity", ["Rice", "Wheat"])
        prediction_month = st.text_input("Prediction month (YYYY-MM)", value="2026-11")
        beneficiaries = st.number_input("Expected beneficiaries", min_value=1, value=500, step=1)
        transactions = st.number_input("Expected transactions", min_value=1, value=400, step=1)

    st.subheader("Stock and storage estimates")
    c3, c4 = st.columns(2)
    with c3:
        opening_stock = st.number_input("Opening stock (kg)", min_value=0.0, value=600.0, step=10.0)
        received_stock = st.number_input("Expected received stock (kg)", min_value=0.0, value=2500.0, step=10.0)
        storage_capacity = st.number_input("Storage capacity (kg)", min_value=1.0, value=1500.0, step=10.0)
        previous_wastage = st.number_input("Previous month's wastage (kg)", min_value=0.0, value=25.0, step=1.0)
    with c4:
        storage_days = st.number_input("Expected storage duration (days)", min_value=1, max_value=90, value=25, step=1)
        delivery_delay = st.number_input("Expected delivery delay (days)", min_value=0, max_value=60, value=7, step=1)
    submitted = st.form_submit_button("Predict distribution and wastage", type="primary", use_container_width=True, disabled=not models_ready())

if submitted:
    try:
        if not state.strip() or not district.strip():
            st.error("Please enter both State and District. Block is optional.")
        else:
            result = predict_food_waste({
                "state": state.strip(), "district": district.strip(), "block": block.strip(),
                "commodity": commodity, "prediction_month": prediction_month.strip(),
                "opening_stock_kg": opening_stock, "received_stock_kg": received_stock,
                "beneficiaries": beneficiaries, "transactions": transactions,
                "storage_capacity_kg": storage_capacity, "storage_days": storage_days,
                "delivery_delay_days": delivery_delay, "previous_wastage_kg": previous_wastage,
            })
            st.subheader("Prediction results")
            m1, m2 = st.columns(2)
            m1.metric("Predicted distributed quantity", f"{result['predicted_distributed_stock_kg']:,.2f} kg")
            m2.metric("Predicted food wastage", f"{result['predicted_wastage_kg']:,.2f} kg")
            st.caption("These are model estimates, not measured values. Accuracy depends on input quality and validation performance.")
    except Exception as exc:
        st.error(f"Could not generate prediction: {exc}")

metrics = load_metrics()
if metrics:
    st.divider()
    st.subheader("Latest chronological test results")
    st.caption(f"Training period: {metrics['train_period'][0]} to {metrics['train_period'][1]} · Test period: {metrics['test_period'][0]} to {metrics['test_period'][1]}")
    a, b = st.columns(2)
    a.metric("Distribution MAE", f"{metrics['stage1_distribution']['mae']:,.2f} kg")
    b.metric("Wastage MAE", f"{metrics['stage2_wastage']['mae']:,.2f} kg")
    with st.expander("View full evaluation metrics"):
        st.json({"Stage 1 — Distribution": metrics["stage1_distribution"], "Stage 2 — Wastage": metrics["stage2_wastage"], "Test rows": metrics["test_rows"], "Stage 2 OOF training rows": metrics["stage2_oof_train_rows"]})
