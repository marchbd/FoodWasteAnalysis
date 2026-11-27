def render_top_nav(active_page):
    import streamlit as st

    st.markdown(
        """
        <style>
        div[data-testid="stPageLink"] a {
            border-radius: 14px !important;
            border: 1px solid #d5e2d2 !important;
            background: linear-gradient(145deg, #fbfdf9, #e9f1e6) !important;
            color: #245334 !important;
            font-weight: 750 !important;
            justify-content: center !important;
            min-height: 44px;
            box-shadow: 5px 5px 12px rgba(151,169,148,.18),
                        -4px -4px 10px rgba(255,255,255,.9) !important;
        }
        div[data-testid="stPageLink"] a:hover {
            border-color: #9fbea0 !important;
            background: #e5efe2 !important;
            transform: translateY(-1px);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    left, right = st.columns(2)
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
