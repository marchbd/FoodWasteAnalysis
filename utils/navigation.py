def render_top_nav(active_page):
    import streamlit as st

    st.markdown(
        """
        <style>
        div[data-testid="stPageLink"] a {
            min-height: 50px; border-radius: 14px !important;
            border: 1px solid #D2D5E4 !important;
            background: linear-gradient(135deg, #FFFFFF, #F1F0FA) !important;
            color: #292E49 !important; font-size: 1rem !important;
            font-weight: 750 !important; justify-content: center !important;
            box-shadow: 0 6px 16px rgba(43,49,78,.09) !important;
            transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease;
        }
        div[data-testid="stPageLink"]:nth-of-type(1) a {
            background: linear-gradient(120deg, #FFF0E8, #FFE0D2) !important;
            border-color: #E8B39F !important;
        }
        div[data-testid="stPageLink"]:nth-of-type(2) a {
            background: linear-gradient(120deg, #F0EBFF, #DFD7FF) !important;
            border-color: #BFB1F0 !important;
        }
        div[data-testid="stPageLink"] a:hover {
            transform: translateY(-4px);
            box-shadow: 0 13px 23px rgba(43,49,78,.16) !important;
            filter: saturate(1.12);
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
