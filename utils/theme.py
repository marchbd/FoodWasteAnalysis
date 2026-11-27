import streamlit as st


def apply_theme():
    """High-contrast multi-colour theme with consistent dark-edged surfaces."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            --ink: #20243A;
            --muted: #525B70;
            --line: #465066;
            --teal: #087F8C;
            --violet: #7356C9;
            --coral: #E56B55;
            --amber: #D99A18;
            --green: #27845A;
            --blue: #3978C8;
            --edge: #485064;
        }
        .stApp {
            color: var(--ink);
            background:
              radial-gradient(ellipse at 5% 2%, rgba(255,190,120,.23), transparent 25%),
              radial-gradient(ellipse at 94% 8%, rgba(153,132,255,.19), transparent 26%),
              radial-gradient(ellipse at 78% 88%, rgba(90,205,190,.13), transparent 28%),
              linear-gradient(145deg, #F8F8FC 0%, #F2F5FB 52%, #FBF6F1 100%);
        }
        [data-testid="stHeader"] { background: rgba(248,249,253,.88); }
        [data-testid="stToolbar"] { right: 1rem; }
        [data-testid="stSidebar"] {
            background: linear-gradient(160deg, #F0EAFE, #E5F3F5 55%, #FFF0E8);
            border-right: 1.5px solid var(--edge);
        }
        [data-testid="stSidebar"] * { color: var(--ink); }
        .block-container { padding-top: 2.25rem; padding-bottom: 3rem; max-width: 1440px; }
        h1, h2, h3, h4 { color: #20243A !important; letter-spacing: -.035em; }
        h1 { font-size: clamp(2rem, 3vw, 2.65rem) !important; font-weight: 820 !important; }
        h2 { font-size: clamp(1.45rem, 2vw, 1.8rem) !important; font-weight: 780 !important; }
        h3 { font-size: 1.2rem !important; font-weight: 750 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: var(--muted); }
        [data-testid="stCaptionContainer"] { font-size: 1rem; line-height: 1.55; color: #525B70; }

        /* Dark, crisp outlines on the shared rounded-card system. */
        [data-testid="stMetric"],
        [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stForm"],
        [data-testid="stExpander"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"],
        [data-testid="stAlert"],
        .st-key-location_period_card,
        .st-key-demand_stock_card,
        .st-key-home_dashboard_link_card,
        .st-key-home_prediction_link_card {
            border: 1.6px solid var(--edge) !important;
            border-radius: 18px !important;
            box-shadow: 0 8px 22px rgba(32,36,58,.10), inset 0 1px 0 rgba(255,255,255,.94) !important;
        }
        [data-testid="stMetric"] {
            padding: 18px 20px;
            border-top: 4px solid var(--violet) !important;
            transition: transform .24s ease, box-shadow .24s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-4px);
            box-shadow: 0 15px 30px rgba(43,49,78,.17) !important;
        }
        [data-testid="stMetricLabel"] { color: #525B70 !important; font-size: .95rem !important; font-weight: 700 !important; }
        [data-testid="stMetricValue"] { color: #292E49 !important; font-weight: 850 !important; }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 14px; }
        div[data-testid="stForm"] { padding: 22px; }
        [data-testid="stExpander"] { background: #FBFAFF !important; }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #FFFFFF !important;
            border: 1.5px solid #596176 !important;
            border-radius: 11px !important;
            box-shadow: inset 0 1px 3px rgba(43,49,78,.045);
            min-height: 42px;
        }
        input, textarea { color: #20243A !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background: #FFFFFF !important; border: 1.5px solid var(--edge) !important;
            border-radius: 12px !important; box-shadow: 0 12px 28px rgba(43,49,78,.18);
        }
        [role="option"] { color: #20243A !important; }
        [role="option"]:hover { background: #F0ECFF !important; }

        .stButton > button, .stFormSubmitButton > button, [data-testid="stDownloadButton"] button {
            min-height: 46px; border-radius: 12px; border: 1.5px solid #282D49;
            background: linear-gradient(115deg, #343B60, #20243A);
            color: #FFFFFF !important; font-weight: 780;
            box-shadow: 0 6px 14px rgba(32,36,58,.24);
            transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
        }
        .stButton > button p, .stFormSubmitButton > button p,
        [data-testid="stDownloadButton"] button p { color: #FFFFFF !important; }
        .stButton > button:hover, .stFormSubmitButton > button:hover,
        [data-testid="stDownloadButton"] button:hover {
            transform: translateY(-2px); filter: brightness(1.12);
            box-shadow: 0 10px 20px rgba(32,36,58,.30); color: #FFFFFF !important;
        }
        .stButton > button:focus-visible, .stFormSubmitButton > button:focus-visible,
        [data-testid="stPageLink"] a:focus-visible {
            outline: 3px solid #E9A23B !important; outline-offset: 3px !important;
        }
        [data-testid="stAlert"] { background: #F7F3FF; }
        [data-testid="stDataFrame"], [data-testid="stTable"] { overflow: hidden; }
        hr { border-color: #B8BECE !important; }
        a { color: #51409A !important; }
        @media (max-width: 700px) { .block-container { padding: 1.25rem 1rem 2rem; } }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
