import streamlit as st


def apply_theme():
    """Apply a vibrant botanical claymorphism theme across the app."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            --bg: #f3f7ef;
            --surface: #fbfdf8;
            --line: #d5e3d0;
            --text: #20392a;
            --muted: #66796b;
            --green: #126b3a;
            --green-mid: #1e9b58;
            --teal: #0f8f83;
            --lime: #b6d943;
            --coral: #e77d50;
        }
        .stApp {
            background:
              radial-gradient(ellipse at 4% 3%, rgba(182,217,67,.23), transparent 27%),
              radial-gradient(ellipse at 96% 8%, rgba(15,143,131,.18), transparent 29%),
              radial-gradient(ellipse at 50% 100%, rgba(30,155,88,.10), transparent 34%),
              linear-gradient(140deg, #f8faf3 0%, #edf5e9 48%, #f7f8ef 100%);
            color: var(--text);
        }
        [data-testid="stHeader"] { background: rgba(248,250,243,.82); }
        [data-testid="stToolbar"] { right: 1rem; }
        [data-testid="stSidebar"] {
            background: linear-gradient(155deg, #e8f3df, #d9eee6 58%, #e8efd4);
            border-right: 1px solid #cbdcc5;
        }
        [data-testid="stSidebar"] * { color: var(--text); }
        .block-container { padding-top: 2.4rem; padding-bottom: 3rem; max-width: 1440px; }
        h1, h2, h3, h4 { color: #174b2d !important; letter-spacing: -.035em; }
        h1 { font-weight: 850 !important; }
        h2, h3 { font-weight: 780 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: #607568; }
        [data-testid="stCaptionContainer"] { color: #718477; }

        [data-testid="stMetric"],
        [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stForm"],
        [data-testid="stExpander"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            background: linear-gradient(145deg, #ffffff, #eaf3e5) !important;
            border: 1px solid rgba(202, 222, 195, .98) !important;
            border-radius: 22px !important;
            box-shadow: 9px 9px 22px rgba(132, 164, 125, .20),
                        -8px -8px 20px rgba(255,255,255,.92),
                        inset 1px 1px 0 rgba(255,255,255,.8) !important;
        }
        [data-testid="stMetric"] {
            padding: 18px 20px;
            border-top: 4px solid #1e9b58 !important;
            transition: transform .22s ease, box-shadow .22s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            box-shadow: 12px 12px 25px rgba(132,164,125,.25),
                        -8px -8px 20px rgba(255,255,255,.95) !important;
        }
        [data-testid="stMetricLabel"] { color: #718477 !important; }
        [data-testid="stMetricValue"] { color: #126b3a !important; font-weight: 850 !important; }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 14px; }
        div[data-testid="stForm"] { padding: 22px; }
        [data-testid="stExpander"] { background: #f2f8ed !important; }

        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #f8fbf4 !important;
            border: 1px solid #cbdcc5 !important;
            border-radius: 13px !important;
            box-shadow: inset 3px 3px 7px rgba(160,184,151,.18),
                        inset -3px -3px 7px rgba(255,255,255,.95);
        }
        input, textarea { color: #263d2d !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background: #fbfdf8 !important;
            border: 1px solid #d1e1cb !important;
            border-radius: 14px !important;
            box-shadow: 8px 8px 20px rgba(132,164,125,.22);
        }
        [role="option"] { color: #263d2d !important; }
        [role="option"]:hover { background: #e3f1dc !important; }

        .stButton > button, .stFormSubmitButton > button, [data-testid="stDownloadButton"] button {
            border-radius: 14px;
            border: 1px solid #126b3a;
            background: linear-gradient(115deg, #159653, #0f766e);
            color: #fff;
            font-weight: 800;
            box-shadow: 5px 5px 12px rgba(18,107,58,.20),
                        -3px -3px 8px rgba(255,255,255,.85),
                        inset 1px 1px 0 rgba(255,255,255,.22);
            transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
        }
        .stButton > button:hover, .stFormSubmitButton > button:hover,
        [data-testid="stDownloadButton"] button:hover {
            transform: translateY(-2px);
            filter: brightness(1.07);
            box-shadow: 7px 7px 15px rgba(18,107,58,.25),
                        -3px -3px 8px rgba(255,255,255,.92);
            color: #fff;
        }
        [data-testid="stAlert"] {
            border-radius: 16px;
            border: 1px solid #d6e7c7;
            background: #f2f8e9;
        }
        [data-testid="stDataFrame"], [data-testid="stTable"] { overflow: hidden; }
        hr { border-color: #d5e5cf !important; }
        a { color: #0f8060 !important; }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
