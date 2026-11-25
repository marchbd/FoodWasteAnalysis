import streamlit as st

st.title("🔮 Food Waste Prediction")
st.caption("Future prediction using the planned two-stage ML pipeline.")

st.info(
    "This form is a UI scaffold only. The prediction models have not been trained "
    "or connected yet. We will finalize the exact fields after auditing the CSV "
    "and confirming which values are known before the prediction month."
)

with st.form("prediction_inputs"):
    st.subheader("Shop and period information")
    col1, col2 = st.columns(2)
    with col1:
        state = st.text_input("State")
        district = st.text_input("District")
        block = st.text_input("Block")
        commodity = st.selectbox("Commodity", ["Rice", "Wheat"])
    with col2:
        shop_id = st.text_input("Shop ID")
        prediction_month = st.text_input("Prediction month (e.g. 2026-12)")
        beneficiaries = st.number_input("Number of beneficiaries", min_value=0, step=1)
        transactions = st.number_input("Expected transactions", min_value=0, step=1)

    st.subheader("Stock and storage information")
    col3, col4 = st.columns(2)
    with col3:
        opening_stock = st.number_input("Opening stock (kg)", min_value=0.0, step=10.0)
        received_stock = st.number_input("Received stock (kg)", min_value=0.0, step=10.0)
        storage_capacity = st.number_input("Storage capacity (kg)", min_value=0.0, step=10.0)
        damaged_stock = st.number_input("Damaged stock (kg)", min_value=0.0, step=1.0)
    with col4:
        storage_days = st.number_input("Expected storage duration (days)", min_value=0, step=1)
        delivery_delay = st.number_input("Expected delivery delay (days)", min_value=0, step=1)
        previous_wastage = st.number_input("Previous wastage (kg)", min_value=0.0, step=1.0)

    submitted = st.form_submit_button("Run prediction", type="primary", use_container_width=True)

if submitted:
    st.warning(
        "Inputs captured in the interface, but prediction is not available until "
        "the two trained models are added. No estimated values are being fabricated."
    )
