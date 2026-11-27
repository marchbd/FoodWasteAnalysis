def render_top_nav(active_page):
    import streamlit as st

    pages = [
        ("home", "Home", "pages/0_Home.py"),
        ("dashboard", "Dashboard", "pages/1_Dashboard.py"),
        ("prediction", "Predict", "pages/2_Food_Waste_Prediction.py"),
    ]

    st.markdown(
        """
        <style>
        .st-key-top-nav {
            padding: 2px 0 10px;
            margin-bottom: 18px;
            border-bottom: 1px solid #D8D6C8;
        }
        .st-key-top-nav [data-testid="stPageLink"] a {
            min-height: 34px !important;
            padding: 4px 2px 7px !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            background: transparent !important;
            border: 0 !important;
            border-bottom: 2px solid transparent !important;
            border-radius: 0 !important;
            box-shadow: none !important;
            color: #68746B !important;
            font-size: .96rem !important;
            font-weight: 500 !important;
            text-decoration: none !important;
        }
        .st-key-top-nav [data-testid="stPageLink"] a *,
        .st-key-top-nav [data-testid="stPageLink"] a p {
            color: #68746B !important;
            -webkit-text-fill-color: #68746B !important;
        }
        .st-key-top-nav .st-key-active-nav [data-testid="stPageLink"] a {
            color: #203A30 !important;
            border-bottom: 2px solid #B85F4C !important;
            font-weight: 750 !important;
        }
        .st-key-top-nav .st-key-active-nav [data-testid="stPageLink"] a *,
        .st-key-top-nav .st-key-active-nav [data-testid="stPageLink"] a p {
            color: #203A30 !important;
            -webkit-text-fill-color: #203A30 !important;
        }
        .st-key-top-nav [data-testid="stPageLink"] a:hover {
            color: #204F3E !important;
            background: transparent !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container(key="top-nav"):
        cols = st.columns(3, gap="small")
        for col, (page_id, label, path) in zip(cols, pages):
            with col:
                if page_id == active_page:
                    with st.container(key="active-nav"):
                        st.page_link(path, label=label, use_container_width=True)
                else:
                    st.page_link(path, label=label, use_container_width=True)
