import streamlit as st


def apply_theme():
    """Warm editorial theme inspired by the supplied mobile design reference."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            --page: #F4F2E9;
            --surface: #FBFAF5;
            --surface-alt: #F0EEE3;
            --ink: #203A30;
            --muted: #657168;
            --green: #204F3E;
            --green-dark: #173F32;
            --green-soft: #E7EADF;
            --line: #D8D6C8;
            --coral: #B85F4C;
        }
        .stApp {
            color: var(--ink);
            background: #F4F2E9 !important;
        }
        [data-testid="stHeader"] { background: #F4F2E9 !important; }
        [data-testid="stToolbar"] { right: 1rem; }
        [data-testid="stSidebar"] {
            background: #EEECE1 !important;
            border-right: 1px solid #D8D6C8;
        }
        [data-testid="stSidebar"] * { color: var(--ink); }
        .block-container {
            padding-top: 1.1rem;
            padding-bottom: 2.5rem;
            max-width: 1440px;
        }
        h1, h2, h3, h4 {
            color: #203A30 !important;
            font-family: Georgia, "Times New Roman", serif !important;
            letter-spacing: -.025em;
        }
        h1 { font-size: clamp(2rem, 3vw, 2.65rem) !important; font-weight: 700 !important; }
        h2 { font-size: clamp(1.4rem, 2vw, 1.8rem) !important; font-weight: 700 !important; }
        h3 { font-size: 1.2rem !important; font-weight: 700 !important; }
        p, label, [data-testid="stCaptionContainer"] {
            color: #56645B;
        }
        [data-testid="stCaptionContainer"] { font-size: 1rem; line-height: 1.5; }

        [data-testid="stMetric"],
        [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stForm"],
        [data-testid="stExpander"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            background: #FBFAF5 !important;
            border: 1px solid #D8D6C8 !important;
            border-radius: 15px !important;
            box-shadow: 0 2px 7px rgba(37,54,44,.045) !important;
        }
        [data-testid="stMetric"] { padding: 16px 18px; }
        [data-testid="stMetricLabel"] {
            color: #69756C !important; font-size: .88rem !important;
            font-weight: 650 !important; letter-spacing: .09em;
            text-transform: uppercase;
        }
        [data-testid="stMetricValue"] {
            color: #204F3E !important; font-family: Georgia, serif !important;
            font-weight: 700 !important;
        }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 14px; }
        div[data-testid="stForm"] { padding: 18px; }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #FFFDF8 !important;
            border: 1px solid #D2D0C3 !important;
            border-radius: 10px !important;
            min-height: 42px;
            box-shadow: none !important;
        }
        input, textarea { color: #293D33 !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background: #FFFDF8 !important;
            border: 1px solid #D2D0C3 !important;
            border-radius: 10px !important;
            box-shadow: 0 8px 20px rgba(32,58,48,.12);
        }
        [role="option"] { color: #293D33 !important; }
        [role="option"]:hover { background: #E9EBDD !important; }

        .stButton > button, .stFormSubmitButton > button,
        [data-testid="stDownloadButton"] button {
            min-height: 44px;
            border-radius: 10px;
            border: 1px solid #173F32 !important;
            background: #204F3E !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            box-shadow: none !important;
            transition: background .18s ease, transform .18s ease;
        }
        .stButton > button p, .stFormSubmitButton > button p,
        [data-testid="stDownloadButton"] button p { color: #FFFFFF !important; }
        .stButton > button:hover, .stFormSubmitButton > button:hover,
        [data-testid="stDownloadButton"] button:hover {
            background: #173F32 !important;
            transform: translateY(-1px);
            color: #FFFFFF !important;
        }
        [data-testid="stAlert"] {
            border-radius: 12px;
            border: 1px solid #D8D6C8;
        }
        hr { border-color: #D8D6C8 !important; }
        a { color: #204F3E !important; }
        @media (max-width: 700px) {
            .block-container { padding: .65rem .85rem 2rem; }
            h1 { font-size: 2rem !important; line-height: 1.12 !important; }
            h2 { font-size: 1.45rem !important; }
            [data-testid="stVerticalBlockBorderWrapper"] { padding: 12px; }
            .st-key-demand_stock_card [data-testid="stHorizontalBlock"],
            .st-key-location_period_card [data-testid="stHorizontalBlock"] {
                flex-wrap: nowrap !important;
                gap: .55rem !important;
            }
            .st-key-demand_stock_card [data-testid="column"],
            .st-key-location_period_card [data-testid="column"] {
                min-width: 0 !important;
                width: 50% !important;
                flex: 1 1 50% !important;
            }
        }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after {
                animation-duration: .01ms !important;
                transition-duration: .01ms !important;
                scroll-behavior: auto !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
