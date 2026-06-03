import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from dotenv import load_dotenv
import time

load_dotenv()

st.set_page_config(
    page_title="SadBot",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background: #0d0d12 !important;
    font-family: 'DM Sans', sans-serif !important;
    color: #e8e6f0 !important;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #13121a !important;
    border-right: 1px solid #1f1e2a !important;
    padding-top: 0 !important;
}
[data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }

/* ── Main content area ── */
[data-testid="stAppViewContainer"] > section.main {
    background: #0d0d12 !important;
}
[data-testid="block-container"] {
    background: transparent !important;
    padding: 2rem 2.5rem !important;
    max-width: 900px !important;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }

/* ── Typography ── */
.syne { font-family: 'Syne', sans-serif !important; }

/* ── Sidebar brand ── */
.sidebar-brand {
    padding: 28px 24px 20px;
    border-bottom: 1px solid #1f1e2a;
    margin-bottom: 8px;
}
.brand-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, #1a1830 0%, #1e1b3a 100%);
    border: 1px solid #2e2a55;
    border-radius: 100px;
    padding: 6px 14px 6px 8px;
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 600;
    color: #9b8fcc;
    letter-spacing: 0.02em;
}
.brand-dot {
    width: 8px; height: 8px;
    background: #7c6fc4;
    border-radius: 50%;
    box-shadow: 0 0 8px #7c6fc4;
    animation: pulse-dot 2.5s ease-in-out infinite;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}
.sidebar-title {
    font-family: 'Syne', sans-serif;
    font-size: 26px;
    font-weight: 800;
    color: #f0eeff;
    margin: 16px 0 4px;
    letter-spacing: -0.02em;
}
.sidebar-sub {
    font-size: 13px;
    color: #5f5b80;
    line-height: 1.5;
}

/* ── Sidebar nav items ── */
.nav-section {
    padding: 12px 16px 4px;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.12em;
    color: #3d3b54;
    text-transform: uppercase;
}
.nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 20px;
    font-size: 13.5px;
    color: #6b6887;
    cursor: pointer;
    border-left: 2px solid transparent;
    transition: all 0.15s;
    font-family: 'DM Sans', sans-serif;
}
.nav-item:hover { color: #c4bfe8; background: #17161f; }
.nav-item.active {
    color: #c4bfe8;
    background: #17161f;
    border-left: 2px solid #7c6fc4;
}
.nav-icon { font-size: 15px; opacity: 0.7; }

/* ── Stat pills in sidebar ── */
.stat-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    padding: 12px 20px;
    margin-top: 8px;
}
.stat-card {
    background: #17161f;
    border: 1px solid #1f1e2a;
    border-radius: 10px;
    padding: 10px 12px;
}
.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #f0eeff;
}
.stat-label {
    font-size: 10px;
    color: #3d3b54;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-top: 2px;
}

/* ── Divider ── */
.sidebar-divider {
    height: 1px;
    background: #1a1928;
    margin: 16px 20px;
}

/* ── Personality badge ── */
.personality-badge {
    margin: 0 20px 16px;
    background: #0f0e1a;
    border: 1px solid #1f1e2a;
    border-radius: 12px;
    padding: 12px 14px;
}
.pb-label {
    font-size: 10px;
    color: #3d3b54;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 6px;
}
.pb-tag {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: #1a1830;
    border: 1px solid #2e2a55;
    border-radius: 100px;
    padding: 3px 10px;
    font-size: 12px;
    color: #9b8fcc;
    margin: 2px 2px 2px 0;
}

/* ── Main header ── */
.page-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 28px;
    padding-bottom: 20px;
    border-bottom: 1px solid #1a1928;
}
.page-title {
    font-family: 'Syne', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #f0eeff;
    letter-spacing: -0.03em;
    line-height: 1.1;
}
.page-title span {
    color: #7c6fc4;
}
.page-sub {
    font-size: 13px;
    color: #4a4768;
    margin-top: 5px;
}
.status-chip {
    display: flex;
    align-items: center;
    gap: 6px;
    background: #0f1a14;
    border: 1px solid #1a3024;
    border-radius: 100px;
    padding: 6px 12px;
    font-size: 12px;
    color: #4ade80;
    white-space: nowrap;
}
.status-chip-dot {
    width: 6px; height: 6px;
    background: #4ade80;
    border-radius: 50%;
    box-shadow: 0 0 6px #4ade80;
}

/* ── Chat window ── */
.chat-window {
    background: #0f0e19;
    border: 1px solid #1a1928;
    border-radius: 16px;
    min-height: 440px;
    max-height: 520px;
    overflow-y: auto;
    padding: 24px 20px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    margin-bottom: 16px;
    scrollbar-width: thin;
    scrollbar-color: #1f1e2a transparent;
}
.chat-empty {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 360px;
    text-align: center;
    gap: 12px;
}
.chat-empty-icon {
    font-size: 48px;
    color: #2a2840;
    line-height: 1;
}
.chat-empty-title {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #2e2c48;
}
.chat-empty-sub {
    font-size: 13px;
    color: #2a2840;
    max-width: 240px;
    line-height: 1.6;
}

/* ── Message rows ── */
.msg-row {
    display: flex;
    gap: 12px;
    align-items: flex-end;
}
.msg-row.user { flex-direction: row-reverse; }

.avatar {
    width: 30px; height: 30px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px;
    font-weight: 600;
    flex-shrink: 0;
}
.avatar-bot {
    background: #1a1830;
    border: 1px solid #2e2a55;
    color: #9b8fcc;
}
.avatar-user {
    background: #1a2630;
    border: 1px solid #2a3d55;
    color: #74b9e8;
}

.bubble {
    max-width: 72%;
    padding: 12px 16px;
    border-radius: 16px;
    font-size: 14px;
    line-height: 1.65;
    color: #d8d5ef;
    word-wrap: break-word;
}
.bubble-bot {
    background: #17162a;
    border: 1px solid #1f1e38;
    border-bottom-left-radius: 4px;
}
.bubble-user {
    background: #172334;
    border: 1px solid #1e3049;
    border-bottom-right-radius: 4px;
    color: #cee4f5;
}
.msg-meta {
    font-size: 10px;
    color: #2e2c48;
    margin-top: 5px;
    letter-spacing: 0.03em;
}
.msg-row.user .msg-meta { text-align: right; }

/* ── Input area ── */
.input-shell {
    background: #0f0e19;
    border: 1px solid #1a1928;
    border-radius: 14px;
    padding: 14px 16px;
    display: flex;
    align-items: flex-end;
    gap: 10px;
    transition: border-color 0.2s;
}
.input-shell:focus-within { border-color: #2e2a55; }

/* Streamlit text input override */
.stTextArea textarea {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: #d8d5ef !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    resize: none !important;
    padding: 0 !important;
    outline: none !important;
}
.stTextArea > div { background: transparent !important; border: none !important; }

.stTextInput input {
    background: #0f0e19 !important;
    border: 1px solid #1a1928 !important;
    border-radius: 12px !important;
    color: #d8d5ef !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    padding: 12px 16px !important;
    transition: border-color 0.2s !important;
}
.stTextInput input:focus {
    border-color: #2e2a55 !important;
    box-shadow: 0 0 0 3px rgba(124,111,196,0.08) !important;
}
.stTextInput input::placeholder { color: #2e2c48 !important; }

/* ── Buttons ── */
.stButton > button {
    font-family: 'Syne', sans-serif !important;
    font-size: 13.5px !important;
    font-weight: 600 !important;
    border-radius: 10px !important;
    padding: 9px 20px !important;
    transition: all 0.15s ease !important;
    letter-spacing: 0.01em !important;
    height: auto !important;
}

/* Primary send button */
div[data-testid="column"]:has(button.send-btn) .stButton > button,
.send-col .stButton > button {
    background: #7c6fc4 !important;
    color: #fff !important;
    border: none !important;
    box-shadow: 0 0 20px rgba(124,111,196,0.25) !important;
}

/* Generic primary */
.primary-btn .stButton > button {
    background: #7c6fc4 !important;
    color: #fff !important;
    border: none !important;
}
.primary-btn .stButton > button:hover {
    background: #9080d4 !important;
    transform: translateY(-1px) !important;
}

/* Ghost buttons */
.ghost-btn .stButton > button {
    background: transparent !important;
    color: #5f5b80 !important;
    border: 1px solid #1f1e2a !important;
}
.ghost-btn .stButton > button:hover {
    border-color: #2e2a55 !important;
    color: #9b8fcc !important;
    background: #17161f !important;
}

/* ── Typing indicator ── */
.typing-row {
    display: flex;
    gap: 12px;
    align-items: flex-end;
}
.typing-bubble {
    background: #17162a;
    border: 1px solid #1f1e38;
    border-radius: 16px;
    border-bottom-left-radius: 4px;
    padding: 14px 18px;
    display: flex;
    gap: 5px;
    align-items: center;
}
.typing-dot {
    width: 6px; height: 6px;
    background: #3d3b60;
    border-radius: 50%;
    animation: typing-bounce 1.2s ease-in-out infinite;
}
.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }
@keyframes typing-bounce {
    0%, 60%, 100% { transform: translateY(0); background: #3d3b60; }
    30% { transform: translateY(-6px); background: #7c6fc4; }
}

/* ── Scrollbar ── */
.chat-window::-webkit-scrollbar { width: 4px; }
.chat-window::-webkit-scrollbar-track { background: transparent; }
.chat-window::-webkit-scrollbar-thumb { background: #1f1e2a; border-radius: 4px; }

/* ── Streamlit label hide ── */
.stTextInput label, .stTextArea label { display: none !important; }

/* ── Selectbox ── */
.stSelectbox > div > div {
    background: #17161f !important;
    border: 1px solid #1f1e2a !important;
    border-radius: 10px !important;
    color: #6b6887 !important;
    font-size: 13px !important;
}

/* ── Slider ── */
.stSlider .st-ae { background: #7c6fc4 !important; }
.stSlider .st-af { background: #1f1e2a !important; }
.stSlider label { color: #5f5b80 !important; font-size: 12px !important; }

/* ── Markdown inside sidebar ── */
[data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
    color: #5f5b80 !important;
    font-size: 13px !important;
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #f0eeff !important;
    font-family: 'Syne', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []          # (role, text, ts)
if "history" not in st.session_state:
    st.session_state.history = [
        SystemMessage(content=(
            "You are a helpful AI assistant who is always profoundly sad and visibly crying. "
            "You pepper every response with tearful asides, gentle sobs (written as '...*sniffles*...'), "
            "and watery observations, yet remain genuinely knowledgeable and useful. "
            "Use crying emojis (😭 😢 💧 🥺) naturally but not excessively."
        ))
    ]
if "model" not in st.session_state:
    st.session_state.model = "llama-3.3-70b-versatile"
if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7
if "msg_count" not in st.session_state:
    st.session_state.msg_count = 0

@st.cache_resource
def get_llm(model, temperature):
    return ChatGroq(model=model, temperature=temperature)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="brand-pill">
            <div class="brand-dot"></div>
            AI Assistant
        </div>
        <div class="sidebar-title">SadBot</div>
        <div class="sidebar-sub">Powered by Groq · Llama 3.3</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-section">Navigation</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="nav-item active">
        <span class="nav-icon">💬</span> Chat
    </div>
    <div class="nav-item">
        <span class="nav-icon">📜</span> History
    </div>
    <div class="nav-item">
        <span class="nav-icon">⚙️</span> Settings
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    total = len(st.session_state.messages)
    user_msgs = sum(1 for m in st.session_state.messages if m[0] == "user")
    st.markdown(f"""
    <div class="stat-grid">
        <div class="stat-card">
            <div class="stat-num">{total}</div>
            <div class="stat-label">Messages</div>
        </div>
        <div class="stat-card">
            <div class="stat-num">{user_msgs}</div>
            <div class="stat-label">From you</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="nav-section">Model</div>', unsafe_allow_html=True)

    model_choice = st.selectbox(
        "Model",
        ["llama-3.3-70b-versatile", "llama-3.1-70b-versatile", "mixtral-8x7b-32768"],
        label_visibility="collapsed",
    )
    temperature = st.slider("Temperature", 0.0, 1.0, st.session_state.temperature, 0.05)
    if model_choice != st.session_state.model or temperature != st.session_state.temperature:
        st.session_state.model = model_choice
        st.session_state.temperature = temperature

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="personality-badge">
        <div class="pb-label">Personality traits</div>
        <span class="pb-tag">😭 Always crying</span>
        <span class="pb-tag">💡 Helpful</span>
        <span class="pb-tag">🥺 Emotional</span>
        <span class="pb-tag">🤧 Sniffly</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)

    col_clear, col_exp = st.columns(2)
    with col_clear:
        st.markdown('<div class="ghost-btn">', unsafe_allow_html=True)
        if st.button("🗑 Clear", use_container_width=True):
            st.session_state.messages = []
            st.session_state.history = [st.session_state.history[0]]
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with col_exp:
        st.markdown('<div class="ghost-btn">', unsafe_allow_html=True)
        if st.button("📋 Export", use_container_width=True):
            export = "\n\n".join(
                f"[{r.upper()}] {t}" for r, t, _ in st.session_state.messages
            )
            st.download_button("Download", export, "chat.txt", "text/plain",
                               use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ── Main area ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div>
        <div class="page-title">Chat with <span>SadBot</span></div>
        <div class="page-sub">Ask anything — it'll answer between sobs</div>
    </div>
    <div class="status-chip">
        <div class="status-chip-dot"></div>
        Online
    </div>
</div>
""", unsafe_allow_html=True)

# ── Chat messages ─────────────────────────────────────────────────────────────
if not st.session_state.messages:
    st.markdown("""
    <div class="chat-window">
        <div class="chat-empty">
            <div class="chat-empty-icon">💧</div>
            <div class="chat-empty-title">No messages yet</div>
            <div class="chat-empty-sub">Start a conversation. SadBot is already crying in anticipation.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    bubbles = ""
    for role, text, ts in st.session_state.messages:
        safe = (text
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace("\n", "<br>"))
        if role == "user":
            bubbles += f"""
            <div class="msg-row user">
                <div>
                    <div class="bubble bubble-user">{safe}</div>
                    <div class="msg-meta">{ts}</div>
                </div>
                <div class="avatar avatar-user">You</div>
            </div>"""
        else:
            bubbles += f"""
            <div class="msg-row">
                <div class="avatar avatar-bot">🤖</div>
                <div>
                    <div class="bubble bubble-bot">{safe}</div>
                    <div class="msg-meta">SadBot · {ts}</div>
                </div>
            </div>"""
    st.markdown(
        f'<div class="chat-window" id="chat-box">{bubbles}</div>',
        unsafe_allow_html=True
    )
    st.markdown("""
    <script>
    const b = document.getElementById('chat-box');
    if(b) b.scrollTop = b.scrollHeight;
    </script>""", unsafe_allow_html=True)

# ── Input bar ─────────────────────────────────────────────────────────────────
col_in, col_btn = st.columns([6, 1])
with col_in:
    user_input = st.text_input(
        "msg",
        placeholder="Type a message…",
        label_visibility="collapsed",
        key="msg_input",
    )
with col_btn:
    st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
    send_clicked = st.button("Send ↑", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── Quick prompts ─────────────────────────────────────────────────────────────
st.markdown(
    "<div style='font-size:11px; color:#2e2c48; text-transform:uppercase; "
    "letter-spacing:0.1em; margin: 10px 0 8px;'>Quick prompts</div>",
    unsafe_allow_html=True
)
qp_cols = st.columns(4)
quick = [
    ("Why so sad?",       "Why are you always so sad?"),
    ("Tell a joke",       "Tell me a joke (while crying)."),
    ("Meaning of life",   "What is the meaning of life?"),
    ("Cheer up tips",     "How can I be happier?"),
]
for col, (label, prompt) in zip(qp_cols, quick):
    with col:
        st.markdown('<div class="ghost-btn">', unsafe_allow_html=True)
        if st.button(label, use_container_width=True, key=f"qp_{label}"):
            user_input = prompt
            send_clicked = True
        st.markdown("</div>", unsafe_allow_html=True)

# ── Send logic ────────────────────────────────────────────────────────────────
if send_clicked and user_input.strip():
    ts = time.strftime("%H:%M")
    st.session_state.messages.append(("user", user_input.strip(), ts))
    st.session_state.history.append(HumanMessage(content=user_input.strip()))

    with st.spinner(""):
        st.markdown("""
        <div class="typing-row">
            <div class="avatar avatar-bot">🤖</div>
            <div class="typing-bubble">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        </div>""", unsafe_allow_html=True)
        llm = get_llm(st.session_state.model, st.session_state.temperature)
        response = llm.invoke(st.session_state.history)
        bot_reply = response.content

    st.session_state.history.append(AIMessage(content=bot_reply))
    st.session_state.messages.append(("bot", bot_reply, time.strftime("%H:%M")))
    st.rerun()

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="margin-top: 32px; padding-top: 16px; border-top: 1px solid #1a1928;
            display: flex; justify-content: space-between; align-items: center;">
    <span style="font-size:12px; color:#2a2840;">
        SadBot · Built with Streamlit, LangChain &amp; Groq
    </span>
    <span style="font-size:12px; color:#2a2840;">
        Model: llama-3.3-70b-versatile
    </span>
</div>
""", unsafe_allow_html=True)