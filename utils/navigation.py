def render_top_nav(active_page):
    import streamlit as st

    st.markdown(
        """
        <style>
        div[data-testid="stPageLink"] a {
            border-radius: 13px !important;
            border: 1px solid rgba(125,211,252,.30) !important;
            background: linear-gradient(115deg, rgba(14,165,233,.16), rgba(124,58,237,.16)) !important;
            color: #edf4ff !important;
            font-weight: 700 !important;
            justify-content: center !important;
            min-height: 42px;
        }
        div[data-testid="stPageLink"] a:hover {
            border-color: rgba(125,211,252,.75) !important;
            background: linear-gradient(115deg, rgba(14,165,233,.30), rgba(124,58,237,.28)) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    left, right = st.columns(2)
    if active_page == "home":
        left.page_link("pages/1_Dashboard.py", label="📊  Dashboard", use_container_width=True)
        right.page_link("pages/2_Food_Waste_Prediction.py", label="🔮  Prediction", use_container_width=True)
    elif active_page == "dashboard":
        left.page_link("pages/0_Home.py", label="🏠  Home", use_container_width=True)
        right.page_link("pages/2_Food_Waste_Prediction.py", label="🔮  Prediction", use_container_width=True)
    else:
        left.page_link("pages/0_Home.py", label="🏠  Home", use_container_width=True)
        right.page_link("pages/1_Dashboard.py", label="📊  Dashboard", use_container_width=True)
    st.write("")
