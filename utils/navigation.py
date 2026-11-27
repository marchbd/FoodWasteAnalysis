def render_top_nav(active_page):
    import streamlit as st

    st.markdown(
        """
        <style>
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-child [data-testid="stPageLink"] a {
            background: linear-gradient(120deg, #174F68, #12394F) !important;
            border: 1.6px solid #102F43 !important;
            color: #FFFFFF !important;
        }
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:last-child [data-testid="stPageLink"] a {
            background: linear-gradient(120deg, #593B83, #39285F) !important;
            border: 1.6px solid #2B1D4C !important;
            color: #FFFFFF !important;
        }
        div[data-testid="stPageLink"] a {
            min-height: 52px; border-radius: 14px !important;
            color: #FFFFFF !important; font-size: 1.02rem !important;
            font-weight: 780 !important; justify-content: center !important;
            text-shadow: 0 1px 1px rgba(0,0,0,.18);
            box-shadow: 0 7px 16px rgba(32,36,58,.20) !important;
            transition: transform .22s ease, box-shadow .22s ease, filter .22s ease;
        }
        div[data-testid="stPageLink"] a p,
        div[data-testid="stPageLink"] a span { color: #FFFFFF !important; }
        div[data-testid="stPageLink"] a:hover {
            transform: translateY(-4px);
            filter: brightness(1.13) saturate(1.12);
            box-shadow: 0 13px 24px rgba(32,36,58,.28) !important;
        }
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
