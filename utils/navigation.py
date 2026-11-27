def render_top_nav(active_page):
    import streamlit as st

    st.markdown(
        """
        <style>
        div[data-testid="stPageLink"] a {
            min-height: 48px;
            border-radius: 13px !important;
            border: 1px solid #8FB29A !important;
            background: linear-gradient(145deg, #FFFFFF, #E7F3E7) !important;
            color: #173D2E !important;
            font-size: 1rem !important;
            font-weight: 700 !important;
            justify-content: center !important;
            box-shadow: 0 5px 14px rgba(8,127,91,.12) !important;
            transition: transform .22s ease, box-shadow .22s ease, border-color .22s ease, background .22s ease;
        }
        div[data-testid="stPageLink"] a:hover {
            border-color: #B4D92E !important;
            background: linear-gradient(145deg, #E4F8E9, #CFF2D8) !important;
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(8,127,91,.24) !important;
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
