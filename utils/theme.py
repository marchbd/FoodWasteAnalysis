import streamlit as st


def apply_theme():
    """Apply the shared dark navy / electric-blue visual system."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: dark;
            --bg: #080d18;
            --surface: #111a2b;
            --surface-2: #172338;
            --line: rgba(148, 163, 184, .18);
            --text: #edf4ff;
            --muted: #9aabc4;
            --blue: #38bdf8;
            --violet: #8b5cf6;
        }
        .stApp {
            background:
              radial-gradient(ellipse at 12% 0%, rgba(37,99,235,.13), transparent 34%),
              radial-gradient(ellipse at 92% 8%, rgba(124,58,237,.11), transparent 30%),
              var(--bg);
            color: var(--text);
        }
        [data-testid="stHeader"] { background: rgba(8,13,24,.78); }
        [data-testid="stToolbar"] { right: 1rem; }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0d1728 0%, #101a2d 100%);
            border-right: 1px solid var(--line);
        }
        [data-testid="stSidebar"] * { color: var(--text); }
        .block-container { padding-top: 2.1rem; padding-bottom: 3rem; max-width: 1440px; }
        h1, h2, h3 { color: #f4f8ff !important; letter-spacing: -.035em; }
        h1 { font-weight: 800 !important; }
        h2, h3 { font-weight: 700 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: #c2cee0; }
        [data-testid="stMetric"] {
            background: linear-gradient(145deg, rgba(24,39,62,.96), rgba(15,25,42,.96));
            border: 1px solid var(--line); border-radius: 16px;
            padding: 16px 18px; box-shadow: 0 10px 28px rgba(0,0,0,.16);
            transition: transform .22s ease, border-color .22s ease, box-shadow .22s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-3px); border-color: rgba(56,189,248,.48);
            box-shadow: 0 14px 30px rgba(2,132,199,.12);
        }
        [data-testid="stMetricLabel"] { color: #a9bad2 !important; }
        [data-testid="stMetricValue"] { color: #f8fbff !important; font-weight: 750; }
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(17,26,43,.72); border: 1px solid var(--line);
            border-radius: 18px; padding: 12px;
        }
        div[data-testid="stForm"] {
            background: linear-gradient(145deg, rgba(17,26,43,.96), rgba(13,22,38,.96));
            border: 1px solid var(--line); border-radius: 20px;
            padding: 22px; box-shadow: 0 14px 38px rgba(0,0,0,.18);
        }
        .stButton > button, .stFormSubmitButton > button, [data-testid="stDownloadButton"] button {
            border-radius: 12px; border: 1px solid rgba(56,189,248,.35);
            background: linear-gradient(110deg, #0369a1, #4f46e5);
            color: white; font-weight: 700; transition: all .2s ease;
        }
        .stButton > button:hover, .stFormSubmitButton > button:hover,
        [data-testid="stDownloadButton"] button:hover {
            transform: translateY(-2px); border-color: #7dd3fc;
            box-shadow: 0 8px 22px rgba(59,130,246,.25); color: white;
        }
        div[data-baseweb="select"] > div, div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #0d1728 !important; border-color: #33445f !important;
            border-radius: 11px !important;
        }
        input, textarea { color: #f1f5f9 !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background: #111c30 !important; border: 1px solid #33445f !important;
        }
        [role="option"] { color: #e2e8f0 !important; }
        [role="option"]:hover { background: #243653 !important; }
        [data-testid="stAlert"] {
            border-radius: 14px; border: 1px solid var(--line);
            background: rgba(22,35,56,.86);
        }
        [data-testid="stDataFrame"], [data-testid="stTable"] {
            border: 1px solid var(--line); border-radius: 14px; overflow: hidden;
        }
        [data-testid="stExpander"] {
            border: 1px solid var(--line); border-radius: 14px; background: rgba(17,26,43,.55);
        }
        hr { border-color: var(--line) !important; }
        a { color: #7dd3fc !important; }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
