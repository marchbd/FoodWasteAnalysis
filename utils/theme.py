import streamlit as st


def apply_theme():
    """Consistent, high-contrast editorial theme for the Food Waste Analysis app."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            --page: #F4F7F1;
            --surface: #FFFFFF;
            --surface-warm: #EAF2E8;
            --ink: #172B25;
            --muted: #465A50;
            --line: #9BB8A3;
            --green: #087F5B;
            --green-dark: #07543D;
            --green-soft: #DDF7E8;
            --gold: #E4A11B;
            --coral: #F07855;
            --blue: #3978B8;
        }
        .stApp {
            color: var(--ink);
            background:
              radial-gradient(ellipse at 8% 0%, rgba(194,239,103,.32), transparent 30%),
              radial-gradient(ellipse at 96% 10%, rgba(0,150,105,.20), transparent 28%),
              linear-gradient(145deg, #F8FBF5 0%, #EDF5EB 48%, #F6FAF2 100%);
        }
        [data-testid="stHeader"] { background: rgba(248,246,240,.9); }
        [data-testid="stToolbar"] { right: 1rem; }
        [data-testid="stSidebar"] {
            background: linear-gradient(160deg, #E4F0E4, #D7EADB);
            border-right: 1px solid #9BB8A3;
        }
        [data-testid="stSidebar"] * { color: var(--ink); }
        .block-container { padding-top: 2.25rem; padding-bottom: 3rem; max-width: 1440px; }
        h1, h2, h3, h4 { color: #172B25 !important; letter-spacing: -.035em; }
        h1 { font-size: clamp(2rem, 3vw, 2.65rem) !important; font-weight: 820 !important; }
        h2 { font-size: clamp(1.45rem, 2vw, 1.8rem) !important; font-weight: 780 !important; }
        h3 { font-size: 1.2rem !important; font-weight: 750 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: var(--muted); }
        [data-testid="stCaptionContainer"] { font-size: 1rem; line-height: 1.55; color: #465A50; }

        [data-testid="stMetric"],
        [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stForm"],
        [data-testid="stExpander"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            background: linear-gradient(145deg, #FFFFFF, #EAF4E9) !important;
            border: 1.5px solid #9BB8A3 !important;
            border-radius: 20px !important;
            box-shadow: 0 8px 22px rgba(65,53,36,.08), inset 0 1px 0 rgba(255,255,255,.9) !important;
        }
        [data-testid="stMetric"] {
            padding: 18px 20px;
            border-top: 4px solid #B4D92E !important;
            transition: transform .24s ease, box-shadow .24s ease, border-color .24s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-4px);
            border-color: #9C8A70 !important;
            box-shadow: 0 14px 28px rgba(65,53,36,.14) !important;
        }
        [data-testid="stMetricLabel"] { color: #40594B !important; font-size: .95rem !important; font-weight: 650 !important; }
        [data-testid="stMetricValue"] { color: #07543D !important; font-weight: 850 !important; }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 14px; }
        div[data-testid="stForm"] { padding: 22px; }
        [data-testid="stExpander"] { background: #F8F4EC !important; }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background:  #FFFFFF !important;
            border: 1px solid #8FB29A !important;
            border-radius: 12px !important;
            box-shadow: inset 0 1px 3px rgba(65,53,36,.06);
            min-height: 42px;
        }
        input, textarea { color: #172B25 !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background:  #FFFFFF !important;
            border: 1.5px solid #9BB8A3 !important;
            border-radius: 12px !important;
            box-shadow: 0 12px 28px rgba(65,53,36,.16);
        }
        [role="option"] { color: #172B25 !important; }
        [role="option"]:hover { background: #DDF7E8 !important; }

        .stButton > button, .stFormSubmitButton > button, [data-testid="stDownloadButton"] button {
            min-height: 44px;
            border-radius: 12px;
            border: 1px solid #07543D;
            background: linear-gradient(115deg, #0B9B69, #08724F);
            color: #fff !important;
            font-weight: 750;
            box-shadow: 0 5px 12px rgba(28,98,64,.18);
            transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
        }
        .stButton > button:hover, .stFormSubmitButton > button:hover,
        [data-testid="stDownloadButton"] button:hover {
            transform: translateY(-2px);
            filter: brightness(1.06);
            box-shadow: 0 9px 18px rgba(28,98,64,.23);
            color: #fff !important;
        }
        .stButton > button:focus-visible, .stFormSubmitButton > button:focus-visible,
        [data-testid="stPageLink"] a:focus-visible {
            outline: 3px solid #E4A11B !important;
            outline-offset: 3px !important;
        }
        [data-testid="stAlert"] {
            border-radius: 14px;
            border: 1px solid #9BB8A3;
            background: #F1F8EF;
        }
        [data-testid="stDataFrame"], [data-testid="stTable"] { overflow: hidden; }
        hr { border-color: #C6DCC8 !important; }
        a { color: #087F5B !important; }
        @media (max-width: 700px) {
            .block-container { padding: 1.25rem 1rem 2rem; }
        }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; scroll-behavior: auto !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
