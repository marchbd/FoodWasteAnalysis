import streamlit as st


def apply_theme():
    """Apply the shared multicolour glassmorphism theme."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: dark;
            --bg: #080d18;
            --glass: rgba(20, 30, 52, .52);
            --glass-strong: rgba(23, 34, 58, .72);
            --line: rgba(190, 210, 255, .19);
            --text: #f3f6ff;
            --muted: #b4c1d8;
            --cyan: #67e8f9;
            --blue: #60a5fa;
            --violet: #c4b5fd;
            --pink: #f0abfc;
            --mint: #6ee7b7;
            --amber: #fcd34d;
        }
        .stApp {
            background:
              radial-gradient(ellipse at 8% 4%, rgba(14,165,233,.20), transparent 30%),
              radial-gradient(ellipse at 88% 10%, rgba(168,85,247,.20), transparent 32%),
              radial-gradient(ellipse at 72% 85%, rgba(236,72,153,.10), transparent 30%),
              radial-gradient(ellipse at 18% 92%, rgba(16,185,129,.10), transparent 28%),
              var(--bg);
            color: var(--text);
        }
        [data-testid="stHeader"] { background: rgba(8,13,24,.35); backdrop-filter: blur(18px); }
        [data-testid="stToolbar"] { right: 1rem; }
        [data-testid="stSidebar"] {
            background: linear-gradient(160deg, rgba(14,25,48,.82), rgba(34,20,58,.72));
            border-right: 1px solid var(--line);
            backdrop-filter: blur(24px);
        }
        [data-testid="stSidebar"] * { color: var(--text); }
        .block-container { padding-top: 2.1rem; padding-bottom: 3rem; max-width: 1440px; }
        h1, h2, h3 { color: #f4f8ff !important; letter-spacing: -.035em; }
        h1 { font-weight: 800 !important; }
        h2, h3 { font-weight: 700 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: #d0daeb; }

        /* Glass surfaces */
        [data-testid="stMetric"],
        [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stForm"],
        [data-testid="stExpander"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            background: linear-gradient(135deg, rgba(36,52,82,.58), rgba(20,27,48,.46)) !important;
            border: 1px solid rgba(190,210,255,.20) !important;
            border-radius: 19px !important;
            box-shadow: 0 12px 34px rgba(0,0,0,.20), inset 0 1px 0 rgba(255,255,255,.07);
            backdrop-filter: blur(20px) saturate(145%);
            -webkit-backdrop-filter: blur(20px) saturate(145%);
        }
        [data-testid="stMetric"] {
            padding: 17px 19px;
            transition: transform .24s ease, border-color .24s ease, box-shadow .24s ease;
        }
        [data-testid="stMetric"]:nth-child(4n+1) { border-color: rgba(103,232,249,.32) !important; }
        [data-testid="stMetric"]:nth-child(4n+2) { border-color: rgba(196,181,253,.34) !important; }
        [data-testid="stMetric"]:nth-child(4n+3) { border-color: rgba(240,171,252,.32) !important; }
        [data-testid="stMetric"]:nth-child(4n) { border-color: rgba(110,231,183,.32) !important; }
        [data-testid="stMetric"]:hover {
            transform: translateY(-4px);
            box-shadow: 0 16px 38px rgba(56,189,248,.13), inset 0 1px 0 rgba(255,255,255,.10);
        }
        [data-testid="stMetricLabel"] { color: #c1cde1 !important; }
        [data-testid="stMetricValue"] { color: #ffffff !important; font-weight: 750; }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 12px; }
        div[data-testid="stForm"] { padding: 22px; }
        [data-testid="stExpander"] { background: rgba(25,35,59,.48) !important; }

        /* Inputs */
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: rgba(12,20,38,.62) !important;
            border: 1px solid rgba(148,180,230,.28) !important;
            border-radius: 12px !important;
            backdrop-filter: blur(12px);
        }
        input, textarea { color: #f1f5f9 !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background: rgba(20,30,52,.96) !important;
            border: 1px solid rgba(190,210,255,.22) !important;
            backdrop-filter: blur(20px);
        }
        [role="option"] { color: #e2e8f0 !important; }
        [role="option"]:hover { background: rgba(96,165,250,.22) !important; }

        /* Coloured glass buttons */
        .stButton > button, .stFormSubmitButton > button, [data-testid="stDownloadButton"] button {
            border-radius: 13px;
            border: 1px solid rgba(125,211,252,.42);
            background: linear-gradient(115deg, rgba(14,165,233,.78), rgba(124,58,237,.78));
            color: white; font-weight: 700;
            box-shadow: 0 7px 22px rgba(59,130,246,.15), inset 0 1px 0 rgba(255,255,255,.18);
            backdrop-filter: blur(12px);
            transition: all .22s ease;
        }
        .stButton > button:hover, .stFormSubmitButton > button:hover,
        [data-testid="stDownloadButton"] button:hover {
            transform: translateY(-2px);
            border-color: rgba(255,255,255,.72);
            box-shadow: 0 10px 28px rgba(139,92,246,.28);
            color: white;
        }

        /* Alerts with distinct tinted glass colours */
        [data-testid="stAlert"] {
            border-radius: 16px; border: 1px solid var(--line);
            background: rgba(35,48,75,.58);
            backdrop-filter: blur(18px);
        }
        [data-testid="stAlert"][data-baseweb="notification"] { box-shadow: 0 8px 26px rgba(0,0,0,.13); }
        [data-testid="stDataFrame"], [data-testid="stTable"] { overflow: hidden; }
        hr { border-color: rgba(190,210,255,.18) !important; }
        a { color: #7dd3fc !important; }
        @keyframes glassFloat { 0% { transform: translateY(0); } 50% { transform: translateY(-3px); } 100% { transform: translateY(0); } }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
