import streamlit as st


def apply_theme():
    """Apply the warm, editorial HopeRise-inspired theme with subtle claymorphism."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            --cream: #F4EBDD;
            --sand: #EED4AC;
            --taupe: #B9A78D;
            --gold: #B19C7A;
            --espresso: #0D0B09;
            --brown: #5A4434;
            --green: #2EA334;
            --ink: #30251D;
            --muted: #786B5B;
            --line: #E0D1BC;
        }
        .stApp {
            background:
              radial-gradient(ellipse at 8% 0%, rgba(238,212,172,.40), transparent 31%),
              radial-gradient(ellipse at 96% 12%, rgba(185,167,141,.20), transparent 30%),
              linear-gradient(145deg, #F8F4EC 0%, #F4EBDD 52%, #F7F1E7 100%);
            color: var(--ink);
        }
        [data-testid="stHeader"] { background: rgba(248,244,236,.88); }
        [data-testid="stToolbar"] { right: 1rem; }
        [data-testid="stSidebar"] {
            background: linear-gradient(160deg, #EFE2CD, #E7D7BE);
            border-right: 1px solid #D8C6AA;
        }
        [data-testid="stSidebar"] * { color: var(--ink); }
        .block-container { padding-top: 2.4rem; padding-bottom: 3rem; max-width: 1440px; }
        h1, h2, h3, h4 { color: var(--espresso) !important; letter-spacing: -.035em; }
        h1 { font-weight: 850 !important; }
        h2, h3 { font-weight: 780 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: var(--muted); }
        [data-testid="stCaptionContainer"] { color: #877967; }

        [data-testid="stMetric"],
        [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stForm"],
        [data-testid="stExpander"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            background: linear-gradient(145deg, #FFFCF6, #F0E5D4) !important;
            border: 1.5px solid #B9A184 !important;
            border-radius: 22px !important;
            box-shadow: 8px 8px 20px rgba(111,85,56,.12),
                        -7px -7px 18px rgba(255,255,255,.86),
                        inset 1px 1px 0 rgba(255,255,255,.78) !important;
        }
        [data-testid="stMetric"] {
            padding: 18px 20px;
            border-top: 4px solid var(--gold) !important;
            transition: transform .22s ease, box-shadow .22s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            box-shadow: 11px 11px 23px rgba(111,85,56,.16),
                        -7px -7px 18px rgba(255,255,255,.9) !important;
        }
        [data-testid="stMetricLabel"] { color: #877967 !important; }
        [data-testid="stMetricValue"] { color: var(--brown) !important; font-weight: 850 !important; }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 14px; }
        div[data-testid="stForm"] { padding: 22px; }
        [data-testid="stExpander"] { background: #F7F0E5 !important; }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #FBF7F0 !important;
            border: 1.5px solid #B9A184 !important;
            border-radius: 13px !important;
            box-shadow: inset 3px 3px 7px rgba(151,126,95,.13),
                        inset -3px -3px 7px rgba(255,255,255,.9);
        }
        input, textarea { color: #30251D !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background: #FFFCF6 !important;
            border: 1.5px solid #B9A184 !important;
            border-radius: 14px !important;
            box-shadow: 8px 8px 20px rgba(111,85,56,.16);
        }
        [role="option"] { color: #30251D !important; }
        [role="option"]:hover { background: #F1E3CE !important; }

        .stButton > button, .stFormSubmitButton > button, [data-testid="stDownloadButton"] button {
            border-radius: 14px;
            border: 1px solid #25872C;
            background: linear-gradient(115deg, #36B33D, #25872C);
            color: #fff;
            font-weight: 800;
            box-shadow: 5px 5px 12px rgba(46,163,52,.19),
                        -3px -3px 8px rgba(255,255,255,.82),
                        inset 1px 1px 0 rgba(255,255,255,.2);
            transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
        }
        .stButton > button:hover, .stFormSubmitButton > button:hover,
        [data-testid="stDownloadButton"] button:hover {
            transform: translateY(-2px);
            filter: brightness(1.06);
            box-shadow: 7px 7px 15px rgba(46,163,52,.23),
                        -3px -3px 8px rgba(255,255,255,.9);
            color: #fff;
        }
        [data-testid="stAlert"] {
            border-radius: 16px;
            border: 1.5px solid #B9A184;
            background: #F8F1E5;
        }
        [data-testid="stDataFrame"], [data-testid="stTable"] { overflow: hidden; }
        hr { border-color: #E0D1BC !important; }
        a { color: #278A30 !important; }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
