import streamlit as st


def apply_theme():
    """Bright, high-contrast multi-colour theme for Food Waste Analysis."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            --ink: #20243A;
            --muted: #525B70;
            --line: #D7DCE8;
            --teal: #087F8C;
            --violet: #7356C9;
            --coral: #E56B55;
            --amber: #D99A18;
            --green: #27845A;
            --blue: #3978C8;
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
            border-right: 1px solid #D2D5E4;
        }
        [data-testid="stSidebar"] * { color: var(--ink); }
        .block-container { padding-top: 2.25rem; padding-bottom: 3rem; max-width: 1440px; }
        h1, h2, h3, h4 { color: #20243A !important; letter-spacing: -.035em; }
        h1 { font-size: clamp(2rem, 3vw, 2.65rem) !important; font-weight: 820 !important; }
        h2 { font-size: clamp(1.45rem, 2vw, 1.8rem) !important; font-weight: 780 !important; }
        h3 { font-size: 1.2rem !important; font-weight: 750 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: var(--muted); }
        [data-testid="stCaptionContainer"] { font-size: 1rem; line-height: 1.55; color: #525B70; }

        [data-testid="stMetric"], [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stForm"], [data-testid="stExpander"],
        [data-testid="stDataFrame"], [data-testid="stTable"] {
            background: linear-gradient(145deg, #FFFFFF, #F6F7FB) !important;
            border: 1.5px solid #D4D9E6 !important;
            border-radius: 20px !important;
            box-shadow: 0 9px 24px rgba(43,49,78,.075), inset 0 1px 0 rgba(255,255,255,.96) !important;
        }
        [data-testid="stMetric"] {
            padding: 18px 20px;
            border-top: 4px solid var(--violet) !important;
            transition: transform .24s ease, box-shadow .24s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-4px);
            box-shadow: 0 15px 30px rgba(43,49,78,.14) !important;
        }
        [data-testid="stMetricLabel"] { color: #525B70 !important; font-size: .95rem !important; font-weight: 700 !important; }
        [data-testid="stMetricValue"] { color: #292E49 !important; font-weight: 850 !important; }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 14px; }
        div[data-testid="stForm"] { padding: 22px; }
        [data-testid="stExpander"] { background: #FBFAFF !important; }

        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #FFFFFF !important;
            border: 1px solid #C9CEDD !important;
            border-radius: 12px !important;
            box-shadow: inset 0 1px 3px rgba(43,49,78,.045);
            min-height: 42px;
        }
        input, textarea { color: #20243A !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background: #FFFFFF !important; border: 1px solid #C9CEDD !important;
            border-radius: 12px !important; box-shadow: 0 12px 28px rgba(43,49,78,.16);
        }
        [role="option"] { color: #20243A !important; }
        [role="option"]:hover { background: #F0ECFF !important; }

        .stButton > button, .stFormSubmitButton > button, [data-testid="stDownloadButton"] button {
            min-height: 44px; border-radius: 12px; border: 1px solid #5940AE;
            background: linear-gradient(115deg, #8064DC, #6248BC);
            color: #fff !important; font-weight: 750;
            box-shadow: 0 6px 14px rgba(98,72,188,.22);
            transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
        }
        .stButton > button:hover, .stFormSubmitButton > button:hover,
        [data-testid="stDownloadButton"] button:hover {
            transform: translateY(-2px); filter: brightness(1.07);
            box-shadow: 0 10px 20px rgba(98,72,188,.28); color: #fff !important;
        }
        .stButton > button:focus-visible, .stFormSubmitButton > button:focus-visible,
        [data-testid="stPageLink"] a:focus-visible {
            outline: 3px solid #E9A23B !important; outline-offset: 3px !important;
        }
        [data-testid="stAlert"] {
            border-radius: 14px; border: 1px solid #D6C8F5; background: #F7F3FF;
        }
        [data-testid="stDataFrame"], [data-testid="stTable"] { overflow: hidden; }
        hr { border-color: #D9DDE9 !important; }
        a { color: #6250B5 !important; }
        @media (max-width: 700px) { .block-container { padding: 1.25rem 1rem 2rem; } }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
