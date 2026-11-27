import streamlit as st


def apply_theme():
    """Apply the shared sage-and-emerald claymorphism theme."""
    st.markdown(
        """
        <style>
        :root {
            color-scheme: light;
            --bg: #f4f7f1;
            --surface: #f7faf5;
            --surface-deep: #e8efe5;
            --line: #d8e3d5;
            --text: #24352b;
            --muted: #68796d;
            --green: #166534;
            --green-mid: #21834a;
            --green-bright: #22a85a;
            --sage: #dce9dc;
        }
        .stApp {
            background:
              radial-gradient(ellipse at 8% 0%, rgba(180, 210, 177, .34), transparent 34%),
              radial-gradient(ellipse at 94% 8%, rgba(202, 226, 204, .42), transparent 32%),
              linear-gradient(145deg, #f7f9f4 0%, #edf3eb 55%, #f5f7f1 100%);
            color: var(--text);
        }
        [data-testid="stHeader"] { background: rgba(247,250,245,.78); }
        [data-testid="stToolbar"] { right: 1rem; }
        [data-testid="stSidebar"] {
            background: linear-gradient(155deg, #edf4eb, #e2ecdf);
            border-right: 1px solid var(--line);
        }
        [data-testid="stSidebar"] * { color: var(--text); }
        .block-container { padding-top: 2.4rem; padding-bottom: 3rem; max-width: 1440px; }
        h1, h2, h3, h4 { color: #203c2b !important; letter-spacing: -.035em; }
        h1 { font-weight: 800 !important; }
        h2, h3 { font-weight: 750 !important; }
        p, label, [data-testid="stCaptionContainer"] { color: #5e7063; }
        [data-testid="stCaptionContainer"] { color: #718074; }

        /* Soft clay surfaces: raised outer shadow and subtle inset highlight. */
        [data-testid="stMetric"],
        [data-testid="stVerticalBlockBorderWrapper"],
        div[data-testid="stForm"],
        [data-testid="stExpander"],
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
            background: linear-gradient(145deg, #fbfdf9, #eaf1e7) !important;
            border: 1px solid rgba(210, 224, 207, .95) !important;
            border-radius: 22px !important;
            box-shadow: 9px 9px 22px rgba(151, 169, 148, .22),
                        -8px -8px 20px rgba(255, 255, 255, .88),
                        inset 1px 1px 0 rgba(255,255,255,.72) !important;
        }
        [data-testid="stMetric"] {
            padding: 18px 20px;
            transition: transform .22s ease, box-shadow .22s ease;
        }
        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            box-shadow: 12px 12px 25px rgba(151,169,148,.25),
                        -8px -8px 20px rgba(255,255,255,.9) !important;
        }
        [data-testid="stMetricLabel"] { color: #718074 !important; }
        [data-testid="stMetricValue"] { color: #1d6038 !important; font-weight: 800; }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 14px; }
        div[data-testid="stForm"] { padding: 22px; }
        [data-testid="stExpander"] { background: #f4f8f1 !important; }

        /* Light, tactile inputs. */
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {
            background: #f4f8f1 !important;
            border: 1px solid #d4e1d1 !important;
            border-radius: 13px !important;
            box-shadow: inset 3px 3px 7px rgba(170,188,166,.20),
                        inset -3px -3px 7px rgba(255,255,255,.9);
        }
        input, textarea { color: #26392d !important; }
        [data-baseweb="popover"], [data-baseweb="menu"] {
            background: #f8fbf6 !important;
            border: 1px solid #d7e3d3 !important;
            border-radius: 14px !important;
            box-shadow: 8px 8px 20px rgba(151,169,148,.22);
        }
        [role="option"] { color: #26392d !important; }
        [role="option"]:hover { background: #e2eee0 !important; }

        .stButton > button, .stFormSubmitButton > button, [data-testid="stDownloadButton"] button {
            border-radius: 14px;
            border: 1px solid #17643a;
            background: linear-gradient(145deg, #23864b, #166534);
            color: #fff;
            font-weight: 750;
            box-shadow: 5px 5px 12px rgba(34, 94, 55, .20),
                        -3px -3px 8px rgba(255,255,255,.85),
                        inset 1px 1px 0 rgba(255,255,255,.20);
            transition: transform .2s ease, box-shadow .2s ease, filter .2s ease;
        }
        .stButton > button:hover, .stFormSubmitButton > button:hover,
        [data-testid="stDownloadButton"] button:hover {
            transform: translateY(-2px);
            filter: brightness(1.06);
            box-shadow: 7px 7px 15px rgba(34,94,55,.24),
                        -3px -3px 8px rgba(255,255,255,.9);
            color: #fff;
        }
        [data-testid="stAlert"] {
            border-radius: 16px;
            border: 1px solid #d8e5d4;
            background: #f1f7ef;
        }
        [data-testid="stDataFrame"], [data-testid="stTable"] { overflow: hidden; }
        hr { border-color: #dbe5d8 !important; }
        a { color: #176b3b !important; }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { animation-duration: .01ms !important; transition-duration: .01ms !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
