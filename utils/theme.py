import streamlit as st


def apply_theme():
    """Consistent, high-contrast editorial theme for the Food Waste Analysis app."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            --page: #F5F2EA;
            --surface: #FFFEFA;
            --surface-warm: #F2E8D8;
            --ink: #29251F;
            --muted: #62594D;
            --line: #C9B99F;
            --green: #246B45;
            --green-dark: #174B32;
            --green-soft: #E3EFE5;
            --gold: #C59A54;
            --coral: #C97857;
            --blue: #547F91;
        }
        .stApp {
            color: var(--ink);
            background:
              radial-gradient(ellipse at 8% 0%, rgba(220,196,151,.24), transparent 30%),
              radial-gradient(ellipse at 96% 10%, rgba(93,137,111,.13), transparent 28%),
              linear-gradient(145deg, #F8F6F0 0%, #F2EEE5 52%, #F7F4ED 100%);
        }
        [data-testid="stHeader"] { background: rgba(248,246,240,.9); }
        [data-testid="stToolbar"] { right: 1rem; }
        [data-testid="stSidebar"] {
            background: linear-gradient(160deg, #EAE5D9, #E2EBDD);
            border-right: 1px solid #C9B99F;
        }
        [data-testid="stSidebar"] * { color: var(--ink); }
        .block-container { padding-top: 2.25rem; padding-bottom: 3rem; max-width: 1440px; }
        h1, h2, h3, h4 { color: #29251F !important; letter-spacing: -.035em; }
        h1 { font-size: clamp(2rem, 3vw, 2.65rem) !important; font-weight: 820 !important; }
        h2 { font-size: clamp(1.45rem, 2vw, 1.8rem) !important; font-weight: 780 !important; }
        h3 { font-size: 1.2rem !important; font-weight: 750 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: var(--muted); }
        [data-testid="stCaptionContainer"] { font-size: 1rem; line-height: 1.55; color: #62594D; }

        [data-testid="stMetric"],
        [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stForm"],
        [data-testid="stExpander"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            background: linear-gradient(145deg, #FFFEFA, #F1E9DC) !important;
            border: 1px solid #C9B99F !important;
            border-radius: 20px !important;
            box-shadow: 0 8px 22px rgba(65,53,36,.08), inset 0 1px 0 rgba(255,255,255,.9) !important;
        }
        [data-testid="stMetric"] {
            padding: 18px 20px;
            border-top: 3px solid var(--green) !important;
            transition: transform .24s ease, box-shadow .24s ease, border-color .24s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-4px);
            border-color: #9C8A70 !important;
            box-shadow: 0 14px 28px rgba(65,53,36,.14) !important;
        }
        [data-testid="stMetricLabel"] { color: #62594D !important; font-size: .95rem !important; font-weight: 650 !important; }
        [data-testid="stMetricValue"] { color: #3E3428 !important; font-weight: 850 !important; }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 14px; }
        div[data-testid="stForm"] { padding: 22px; }
        [data-testid="stExpander"] { background: #F8F4EC !important; }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #FFFEFA !important;
            border: 1px solid #BDAE96 !important;
            border-radius: 12px !important;
            box-shadow: inset 0 1px 3px rgba(65,53,36,.06);
            min-height: 42px;
        }
        input, textarea { color: #29251F !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background: #FFFEFA !important;
            border: 1px solid #C9B99F !important;
            border-radius: 12px !important;
            box-shadow: 0 12px 28px rgba(65,53,36,.16);
        }
        [role="option"] { color: #29251F !important; }
        [role="option"]:hover { background: #E8F0E7 !important; }

        .stButton > button, .stFormSubmitButton > button, [data-testid="stDownloadButton"] button {
            min-height: 44px;
            border-radius: 12px;
            border: 1px solid #174B32;
            background: linear-gradient(115deg, #2D8052, #1C6240);
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
            outline: 3px solid #C59A54 !important;
            outline-offset: 3px !important;
        }
        [data-testid="stAlert"] {
            border-radius: 14px;
            border: 1px solid #C9B99F;
            background: #F8F4EC;
        }
        [data-testid="stDataFrame"], [data-testid="stTable"] { overflow: hidden; }
        hr { border-color: #D8CBB7 !important; }
        a { color: #246B45 !important; }
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
