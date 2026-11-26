import streamlit as st

st.set_page_config(page_title="Food Waste Analysis", page_icon="🍚", layout="wide", initial_sidebar_state="collapsed")

home_page = st.Page("pages/0_Home.py", title="Home", icon="🏠", default=True)
dashboard_page = st.Page("pages/1_Dashboard.py", title="Dashboard", icon="📊")
prediction_page = st.Page("pages/2_Food_Waste_Prediction.py", title="Prediction", icon="🔮")

navigation = st.navigation(
    [home_page, dashboard_page, prediction_page],
    position="hidden",
)
navigation.run()
