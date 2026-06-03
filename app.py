import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv
import time

load_dotenv()

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Nova AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cabinet+Grotesk:wght@400;500;700;800;900&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --c1: #ff6b6b;
    --c2: #ffd93d;
    --c3: #6bcb77;
    --c4: #4d96ff;
    --c5: #c77dff;
    --c6: #ff9a3c;
    --bg:  #09090f;
    --bg2: #0f0f1a;
    --bg3: #141422;
    --border: rgba(255,255,255,0.07);
    --text: #f0eeff;
    --muted: #5a576e;
    --font-display: 'Cabinet Grotesk', sans-serif;
    --font-body: 'Instrument Sans', sans-serif;
}

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background: var(--bg) !important;
    font-family: var(--font-body) !important;
    color: var(--text) !important;
}
[data-testid="stAppViewContainer"] > section.main { background: var(--bg) !important; }
[data-testid="block-container"] {
    background: transparent !important;
    padding: 1.5rem 2rem !important;
    max-width: 860px !important;
}
#MainMenu, footer, header, [data-testid="stToolbar"] { visibility: hidden; display: none; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }

/* ── Sidebar brand area ── */
.sb-top {
    padding: 28px 22px 22px;
    position: relative;
    overflow: hidden;
}
.sb-top::before {
    content: '';
    position: absolute;
    top: -60px; left: -60px;
    width: 180px; height: 180px;
    background: radial-gradient(circle, rgba(77,150,255,0.18) 0%, transparent 70%);
    pointer-events: none;
}
.sb-top::after {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 140px; height: 140px;
    background: radial-gradient(circle, rgba(199,125,255,0.15) 0%, transparent 70%);
    pointer-events: none;
}
.logo-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
    position: relative; z-index: 1;
}
.logo-gem {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, var(--c4), var(--c5));
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
    box-shadow: 0 0 18px rgba(77,150,255,0.4);
    animation: gem-pulse 3s ease-in-out infinite;
}
@keyframes gem-pulse {
    0%, 100% { box-shadow: 0 0 18px rgba(77,150,255,0.4); }
    50%       { box-shadow: 0 0 32px rgba(77,150,255,0.7), 0 0 60px rgba(199,125,255,0.2); }
}
.logo-name {
    font-family: var(--font-display);
    font-size: 22px;
    font-weight: 900;
    background: linear-gradient(90deg, var(--c4), var(--c5));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.02em;
}
.sb-tagline {
    font-size: 12px;
    color: var(--muted);
    position: relative; z-index: 1;
    line-height: 1.5;
}

.sb-divider {
    height: 1px;
    background: var(--border);
    margin: 4px 0;
}

/* ── Stats row ── */
.stats-row {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 8px;
    padding: 14px 22px;
}
.stat-box {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 10px 8px;
    text-align: center;
}
.stat-n {
    font-family: var(--font-display);
    font-size: 22px;
    font-weight: 800;
    line-height: 1;
}
.stat-l {
    font-size: 9px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-top: 3px;
}

/* ── Nav ── */
.nav-label {
    padding: 14px 22px 6px;
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 0.14em;
    color: var(--muted);
    text-transform: uppercase;
}
.nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 22px;
    font-size: 13.5px;
    color: var(--muted);
    border-left: 2px solid transparent;
    cursor: pointer;
    font-family: var(--font-body);
    transition: all 0.15s;
}
.nav-item.active {
    color: var(--text);
    border-left: 2px solid var(--c4);
    background: rgba(77,150,255,0.06);
}
.nav-item:hover:not(.active) {
    color: rgba(240,238,255,0.7);
    background: rgba(255,255,255,0.03);
}

/* ── Model selector label ── */
.sb-section-title {
    padding: 16px 22px 6px;
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 0.14em;
    color: var(--muted);
    text-transform: uppercase;
}

/* ── Streamlit widgets override ── */
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: var(--bg3) !important;
    border: 1px solid var(--border) !important;
    border-radius: 9px !important;
    color: rgba(240,238,255,0.65) !important;
    font-family: var(--font-body) !important;
    font-size: 13px !important;
}
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stSlider label {
    color: var(--muted) !important;
    font-size: 11px !important;
    font-family: var(--font-body) !important;
}
[data-testid="stSidebar"] .stSlider [data-testid="stThumbValue"] {
    color: var(--c4) !important;
}

/* ── Color swatches for gradient picker ── */
.theme-row {
    display: flex;
    gap: 7px;
    padding: 8px 22px 16px;
}
.swatch {
    width: 22px; height: 22px;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid transparent;
    transition: transform 0.15s;
}
.swatch:hover { transform: scale(1.2); }
.swatch.active { border-color: rgba(255,255,255,0.6); }

/* ── Main page header ── */
.page-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 22px;
    padding-bottom: 18px;
    border-bottom: 1px solid var(--border);
}
.page-title {
    font-family: var(--font-display);
    font-size: 26px;
    font-weight: 900;
    letter-spacing: -0.03em;
    background: linear-gradient(90deg, var(--c4) 0%, var(--c5) 50%, var(--c1) 100%);
    background-size: 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: title-shift 5s linear infinite;
}
@keyframes title-shift {
    0%   { background-position: 0%; }
    100% { background-position: 200%; }
}
.page-sub { font-size: 13px; color: var(--muted); margin-top: 3px; }
.live-badge {
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(107,203,119,0.1);
    border: 1px solid rgba(107,203,119,0.25);
    border-radius: 100px;
    padding: 5px 12px;
    font-size: 12px;
    color: var(--c3);
    font-family: var(--font-body);
}
.live-dot {
    width: 6px; height: 6px;
    background: var(--c3);
    border-radius: 50%;
    animation: blink 1.8s ease-in-out infinite;
}
@keyframes blink {
    0%,100% { opacity: 1; }
    50%      { opacity: 0.3; }
}

/* ── Chat window ── */
.chat-win {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 18px;
    min-height: 420px;
    max-height: 500px;
    overflow-y: auto;
    padding: 22px 18px;
    display: flex;
    flex-direction: column;
    gap: 18px;
    margin-bottom: 14px;
    scrollbar-width: thin;
    scrollbar-color: #1e1e30 transparent;
}
.chat-win::-webkit-scrollbar { width: 4px; }
.chat-win::-webkit-scrollbar-thumb { background: #1e1e30; border-radius: 4px; }

/* ── Empty state ── */
.empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 340px;
    gap: 14px;
    text-align: center;
}
.empty-orb {
    width: 72px; height: 72px;
    border-radius: 50%;
    background: linear-gradient(135deg, rgba(77,150,255,0.15), rgba(199,125,255,0.15));
    border: 1px solid rgba(77,150,255,0.2);
    display: flex; align-items: center; justify-content: center;
    font-size: 32px;
    animation: orb-float 3s ease-in-out infinite;
}
@keyframes orb-float {
    0%,100% { transform: translateY(0); }
    50%      { transform: translateY(-8px); }
}
.empty-title {
    font-family: var(--font-display);
    font-size: 18px;
    font-weight: 700;
    color: rgba(240,238,255,0.3);
}
.empty-sub { font-size: 13px; color: var(--muted); max-width: 220px; line-height: 1.6; }

/* ── Message rows ── */
.mrow { display: flex; gap: 10px; align-items: flex-end; }
.mrow.user { flex-direction: row-reverse; }

.av {
    width: 28px; height: 28px;
    border-radius: 8px;
    flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px;
    font-weight: 700;
}
.av-ai {
    background: linear-gradient(135deg, rgba(77,150,255,0.25), rgba(199,125,255,0.25));
    border: 1px solid rgba(77,150,255,0.3);
    color: var(--c4);
}
.av-u {
    background: linear-gradient(135deg, rgba(255,107,107,0.2), rgba(255,211,61,0.2));
    border: 1px solid rgba(255,211,61,0.25);
    color: var(--c2);
}

.bbl {
    max-width: 74%;
    padding: 11px 15px;
    border-radius: 16px;
    font-size: 14px;
    line-height: 1.68;
    word-wrap: break-word;
    animation: msg-in 0.22s cubic-bezier(.34,1.56,.64,1);
}
@keyframes msg-in {
    from { transform: scale(0.9) translateY(6px); opacity: 0; }
    to   { transform: scale(1) translateY(0);      opacity: 1; }
}
.bbl-ai {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-bottom-left-radius: 4px;
    color: rgba(240,238,255,0.88);
}
.bbl-u {
    background: linear-gradient(135deg, rgba(77,150,255,0.18), rgba(199,125,255,0.14));
    border: 1px solid rgba(77,150,255,0.2);
    border-bottom-right-radius: 4px;
    color: rgba(240,238,255,0.9);
}
.msg-time { font-size: 9px; color: var(--muted); margin-top: 4px; }
.mrow.user .msg-time { text-align: right; }

/* ── Typing dots ── */
.typing-bbl {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 16px;
    border-bottom-left-radius: 4px;
    padding: 13px 16px;
    display: flex; gap: 5px; align-items: center;
}
.td {
    width: 6px; height: 6px;
    border-radius: 50%;
    animation: tdot 1.2s ease-in-out infinite;
}
.td:nth-child(1) { background: var(--c4); }
.td:nth-child(2) { background: var(--c5); animation-delay: .2s; }
.td:nth-child(3) { background: var(--c1); animation-delay: .4s; }
@keyframes tdot {
    0%,60%,100% { transform: translateY(0); opacity: 0.4; }
    30%          { transform: translateY(-7px); opacity: 1; }
}

/* ── Input area ── */
.stTextInput > div > div > input {
    background: var(--bg2) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
    font-family: var(--font-body) !important;
    font-size: 14px !important;
    padding: 13px 18px !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
    caret-color: var(--c4) !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(77,150,255,0.45) !important;
    box-shadow: 0 0 0 3px rgba(77,150,255,0.08) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder { color: var(--muted) !important; }
.stTextInput label { display: none !important; }

/* ── Buttons ── */
.stButton > button {
    font-family: var(--font-display) !important;
    font-weight: 700 !important;
    font-size: 13.5px !important;
    border-radius: 10px !important;
    padding: 10px 18px !important;
    transition: all 0.18s ease !important;
    letter-spacing: 0.01em !important;
    height: auto !important;
    line-height: 1.2 !important;
}
.btn-send .stButton > button {
    background: linear-gradient(135deg, var(--c4), var(--c5)) !important;
    color: #fff !important;
    border: none !important;
    box-shadow: 0 4px 20px rgba(77,150,255,0.3) !important;
}
.btn-send .stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(77,150,255,0.45) !important;
}
.btn-ghost .stButton > button {
    background: transparent !important;
    color: var(--muted) !important;
    border: 1px solid var(--border) !important;
}
.btn-ghost .stButton > button:hover {
    border-color: rgba(77,150,255,0.3) !important;
    color: var(--c4) !important;
    background: rgba(77,150,255,0.06) !important;
}
.btn-danger .stButton > button {
    background: rgba(255,107,107,0.08) !important;
    color: var(--c1) !important;
    border: 1px solid rgba(255,107,107,0.2) !important;
}
.btn-danger .stButton > button:hover {
    background: rgba(255,107,107,0.15) !important;
}

/* ── Quick prompts ── */
.qp-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: var(--muted);
    text-transform: uppercase;
    margin: 12px 0 7px;
}
.qp-wrap {
    display: flex; flex-wrap: wrap; gap: 7px;
    margin-bottom: 6px;
}
.qp-chip {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 5px 12px;
    border-radius: 100px;
    font-size: 12.5px;
    color: rgba(240,238,255,0.55);
    border: 1px solid var(--border);
    cursor: pointer;
    background: var(--bg2);
    font-family: var(--font-body);
    transition: all 0.15s;
}
.qp-chip:hover { color: var(--text); border-color: rgba(77,150,255,0.35); background: rgba(77,150,255,0.06); }

/* ── Accent line at top ── */
.accent-bar {
    height: 3px;
    background: linear-gradient(90deg, var(--c1), var(--c2), var(--c3), var(--c4), var(--c5), var(--c6), var(--c1));
    background-size: 300%;
    animation: bar-slide 4s linear infinite;
    border-radius: 0 0 3px 3px;
    margin-bottom: 0;
}
@keyframes bar-slide {
    0%   { background-position: 0%; }
    100% { background-position: 300%; }
}

/* ── Footer ── */
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 28px;
    padding-top: 14px;
    border-top: 1px solid var(--border);
    font-size: 11px;
    color: var(--muted);
}
.footer-dot { margin: 0 6px; opacity: 0.4; }

/* Selectbox arrow */
[data-testid="stSidebar"] .stSelectbox svg { color: var(--muted) !important; }
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []            # (role, text, ts)
if "history" not in st.session_state:
    st.session_state.history = [
        SystemMessage(content="You are a helpful, knowledgeable, and friendly AI chatbot called Nova. Be concise, clear, and engaging.")
    ]
if "model" not in st.session_state:
    st.session_state.model = "llama-3.3-70b-versatile"
if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7

@st.cache_resource
def get_llm(model, temp):
    return ChatGroq(model=model, temperature=temp)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="accent-bar"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="sb-top">
        <div class="logo-row">
            <div class="logo-gem">✦</div>
            <div class="logo-name">Nova AI</div>
        </div>
        <div class="sb-tagline">Powered by Groq · Llama 3.3 · LangChain<br>Fast. Smart. Always on.</div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    total = len(st.session_state.messages)
    you   = sum(1 for m in st.session_state.messages if m[0] == "user")
    ai    = total - you
    st.markdown(f"""
    <div class="stats-row">
        <div class="stat-box">
            <div class="stat-n" style="color:var(--c4)">{total}</div>
            <div class="stat-l">Total</div>
        </div>
        <div class="stat-box">
            <div class="stat-n" style="color:var(--c2)">{you}</div>
            <div class="stat-l">Yours</div>
        </div>
        <div class="stat-box">
            <div class="stat-n" style="color:var(--c5)">{ai}</div>
            <div class="stat-l">AI</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="nav-label">Navigation</div>
    <div class="nav-item active">💬&nbsp;&nbsp;Chat</div>
    <div class="nav-item">📚&nbsp;&nbsp;History</div>
    <div class="nav-item">🎨&nbsp;&nbsp;Personas</div>
    <div class="nav-item">⚙️&nbsp;&nbsp;Settings</div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

    # Model config
    st.markdown('<div class="sb-section-title">Model</div>', unsafe_allow_html=True)
    model_choice = st.selectbox(
        "model",
        ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768", "gemma2-9b-it"],
        label_visibility="collapsed",
    )
    st.markdown('<div class="sb-section-title">Temperature</div>', unsafe_allow_html=True)
    temperature = st.slider("temp", 0.0, 1.0, st.session_state.temperature, 0.05,
                            label_visibility="collapsed")

    if model_choice != st.session_state.model or temperature != st.session_state.temperature:
        st.session_state.model = model_choice
        st.session_state.temperature = temperature

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

    # System prompt
    st.markdown('<div class="sb-section-title">System prompt</div>', unsafe_allow_html=True)
    sys_prompt = st.text_area(
        "sys",
        value="You are a helpful, knowledgeable, and friendly AI chatbot called Nova. Be concise, clear, and engaging.",
        height=90,
        label_visibility="collapsed",
    )
    if st.button("Apply prompt", use_container_width=True):
        st.session_state.history = [SystemMessage(content=sys_prompt)]
        st.session_state.messages = []
        st.rerun()

    st.markdown('<div class="sb-divider"></div>', unsafe_allow_html=True)

    # Action buttons
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="btn-danger">', unsafe_allow_html=True)
        if st.button("🗑 Clear", use_container_width=True):
            st.session_state.messages = []
            st.session_state.history  = [st.session_state.history[0]]
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="btn-ghost">', unsafe_allow_html=True)
        if st.button("⬇ Export", use_container_width=True):
            txt = "\n\n".join(f"[{r.upper()}] {t}" for r, t, _ in st.session_state.messages)
            st.download_button("Save .txt", txt, "nova_chat.txt", "text/plain",
                               use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ── Main ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-head">
    <div>
        <div class="page-title">Nova AI Chat</div>
        <div class="page-sub">Ask anything. Get brilliant answers instantly.</div>
    </div>
    <div class="live-badge">
        <div class="live-dot"></div>
        Live
    </div>
</div>
""", unsafe_allow_html=True)

# ── Chat window ───────────────────────────────────────────────────────────────
if not st.session_state.messages:
    chat_html = """
    <div class="empty-state">
        <div class="empty-orb">✦</div>
        <div class="empty-title">Nova is ready</div>
        <div class="empty-sub">Start typing below or pick a quick prompt to begin.</div>
    </div>"""
else:
    chat_html = ""
    for role, text, ts in st.session_state.messages:
        safe = (text.replace("&", "&amp;")
                    .replace("<", "&lt;")
                    .replace(">", "&gt;")
                    .replace("\n", "<br>"))
        if role == "user":
            chat_html += f"""
            <div class="mrow user">
                <div>
                    <div class="bbl bbl-u">{safe}</div>
                    <div class="msg-time">{ts}</div>
                </div>
                <div class="av av-u">You</div>
            </div>"""
        else:
            chat_html += f"""
            <div class="mrow">
                <div class="av av-ai">✦</div>
                <div>
                    <div class="bbl bbl-ai">{safe}</div>
                    <div class="msg-time">Nova · {ts}</div>
                </div>
            </div>"""

st.markdown(
    f'<div class="chat-win" id="cw">{chat_html}</div>',
    unsafe_allow_html=True
)
st.markdown("""
<script>
const cw = document.getElementById('cw');
if(cw) cw.scrollTop = cw.scrollHeight;
</script>""", unsafe_allow_html=True)

# ── Input row ─────────────────────────────────────────────────────────────────
ic, bc = st.columns([6, 1])
with ic:
    user_input = st.text_input("msg", placeholder="Message Nova…",
                               label_visibility="collapsed", key="user_msg")
with bc:
    st.markdown('<div class="btn-send">', unsafe_allow_html=True)
    send = st.button("Send ↑", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── Quick prompts ─────────────────────────────────────────────────────────────
st.markdown('<div class="qp-label">Quick prompts</div>', unsafe_allow_html=True)
qp_cols = st.columns(4)
quick = [
    ("✨ Explain AI",    "Explain artificial intelligence in simple terms."),
    ("🌍 Fun fact",      "Tell me a fascinating fact about the universe."),
    ("💡 Startup idea",  "Give me a unique startup idea for 2025."),
    ("📝 Write a poem",  "Write a short inspiring poem about the future."),
]
for col, (label, prompt) in zip(qp_cols, quick):
    with col:
        st.markdown('<div class="btn-ghost">', unsafe_allow_html=True)
        if st.button(label, use_container_width=True, key=f"qp_{label}"):
            user_input = prompt
            send = True
        st.markdown("</div>", unsafe_allow_html=True)

# ── Send logic ────────────────────────────────────────────────────────────────
if send and user_input.strip():
    ts = time.strftime("%H:%M")
    st.session_state.messages.append(("user", user_input.strip(), ts))
    st.session_state.history.append(HumanMessage(content=user_input.strip()))

    with st.spinner(""):
        # Show typing indicator
        st.markdown("""
        <div class="mrow" style="margin-top:8px">
            <div class="av av-ai">✦</div>
            <div class="typing-bbl">
                <div class="td"></div>
                <div class="td"></div>
                <div class="td"></div>
            </div>
        </div>""", unsafe_allow_html=True)
        llm = get_llm(st.session_state.model, st.session_state.temperature)
        response = llm.invoke(st.session_state.history)
        reply = response.content

    st.session_state.history.append(AIMessage(content=reply))
    st.session_state.messages.append(("bot", reply, time.strftime("%H:%M")))
    st.rerun()

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
    <span>Nova AI &nbsp;·&nbsp; Built with Streamlit &amp; LangChain</span>
    <span>Model: {st.session_state.model}<span class="footer-dot">•</span>Groq</span>
</div>
""", unsafe_allow_html=True)