def render_top_nav(active_page):
    import streamlit as st

    st.markdown(
        """
        <style>
        div[data-testid="stPageLink"] a {
            min-height: 48px;
            border-radius: 13px !important;
            border: 1px solid #C9B99F !important;
            background: linear-gradient(145deg, #FFFEFA, #F0E8DA) !important;
            color: #43392D !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
            justify-content: center !important;
            box-shadow: 0 5px 14px rgba(65,53,36,.08) !important;
            transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease, background .22s ease;
        }
        div[data-testid="stPageLink"] a:hover {
            border-color: #78947B !important;
            background: linear-gradient(145deg, #F4F8F1, #E5EFE3) !important;
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(36,107,69,.14) !important;
        }
        div[data-testid="stPageLink"] a p { color: inherit !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    left, right = st.columns(2, gap="large")
    if active_page == "home":
        left.page_link("pages/1_Dashboard.py", label="Dashboard", use_container_width=True)
        right.page_link("pages/2_Food_Waste_Prediction.py", label="Food Waste Prediction", use_container_width=True)
    elif active_page == "dashboard":
        left.page_link("pages/0_Home.py", label="Home", use_container_width=True)
        right.page_link("pages/2_Food_Waste_Prediction.py", label="Food Waste Prediction", use_container_width=True)
    else:
        left.page_link("pages/0_Home.py", label="Home", use_container_width=True)
        right.page_link("pages/1_Dashboard.py", label="Dashboard", use_container_width=True)
    st.write("")
