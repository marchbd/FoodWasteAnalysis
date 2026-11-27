def render_top_nav(active_page):
    import streamlit as st

    st.markdown(
        """
        <style>
        /* Scope each link to its own keyed container so other app buttons stay untouched. */
        .st-key-nav-primary [data-testid="stPageLink"] a {
            background: linear-gradient(120deg, #172B4D 0%, #101C35 100%) !important;
            border: 1.7px solid #0A1428 !important;
        }
        .st-key-nav-secondary [data-testid="stPageLink"] a {
            background: linear-gradient(120deg, #43245F 0%, #28143F 100%) !important;
            border: 1.7px solid #1D0D30 !important;
        }
        .st-key-nav-primary [data-testid="stPageLink"] a,
        .st-key-nav-secondary [data-testid="stPageLink"] a {
            min-height: 54px !important;
            border-radius: 14px !important;
            color: #FFFFFF !important;
            font-size: 1.03rem !important;
            font-weight: 800 !important;
            justify-content: center !important;
            text-shadow: 0 1px 2px rgba(0,0,0,.28);
            box-shadow: 0 8px 18px rgba(20,25,48,.24) !important;
            transition: transform .22s ease, box-shadow .22s ease, filter .22s ease;
        }
        .st-key-nav-primary [data-testid="stPageLink"] a *,
        .st-key-nav-secondary [data-testid="stPageLink"] a * {
            color: #FFFFFF !important;
            -webkit-text-fill-color: #FFFFFF !important;
        }
        .st-key-nav-primary [data-testid="stPageLink"] a:hover,
        .st-key-nav-secondary [data-testid="stPageLink"] a:hover {
            transform: translateY(-3px);
            filter: brightness(1.18) saturate(1.12);
            box-shadow: 0 13px 25px rgba(20,25,48,.32) !important;
        }
        .st-key-nav-primary [data-testid="stPageLink"] a:focus-visible,
        .st-key-nav-secondary [data-testid="stPageLink"] a:focus-visible {
            outline: 3px solid #E9A23B !important;
            outline-offset: 3px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns(2, gap="large")
    if active_page == "home":
        with left.container(key="nav-primary"):
            st.page_link("pages/1_Dashboard.py", label="Dashboard", use_container_width=True)
        with right.container(key="nav-secondary"):
            st.page_link("pages/2_Food_Waste_Prediction.py", label="Food Waste Prediction", use_container_width=True)
    elif active_page == "dashboard":
        with left.container(key="nav-primary"):
            st.page_link("pages/0_Home.py", label="Home", use_container_width=True)
        with right.container(key="nav-secondary"):
            st.page_link("pages/2_Food_Waste_Prediction.py", label="Food Waste Prediction", use_container_width=True)
    else:
        with left.container(key="nav-primary"):
            st.page_link("pages/0_Home.py", label="Home", use_container_width=True)
        with right.container(key="nav-secondary"):
            st.page_link("pages/1_Dashboard.py", label="Dashboard", use_container_width=True)
    st.write("")
