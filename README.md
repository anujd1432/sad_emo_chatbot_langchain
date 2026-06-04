# ✦ Nova AI — Your Brilliant Chat Companion

<div align="center">

![Nova AI Banner](https://img.shields.io/badge/Nova%20AI-Powered%20by%20Groq-4d96ff?style=for-the-badge&logo=lightning&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-ffd93d?style=for-the-badge&logo=python&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-ff6b6b?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-🦜-6bcb77?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-c77dff?style=for-the-badge)

**⚡ Fast. 🧠 Smart. 🌟 Always On.**

*A sleek, dark-themed AI chatbot built with Streamlit, powered by Groq's blazing-fast inference and LangChain.*

[🚀 Quick Start](#-quick-start) · [✨ Features](#-features) · [🛠 Tech Stack](#-tech-stack) · [📸 Screenshots](#-screenshots) · [🤝 Contributing](#-contributing)

</div>
---
link live: https://sademochatbotlangchain-zrq9nvzchl6mkrjb25yqsd.streamlit.app

---

## 🌟 What is Nova AI?

Nova AI is a **gorgeous, production-ready AI chatbot** interface that puts the power of large language models right at your fingertips. With a stunning dark UI, animated accents, and real-time responses powered by **Groq's ultra-fast inference engine**, chatting with Nova feels smooth, fast, and delightful.

> 💬 *"Ask anything. Get brilliant answers instantly."*

---

## ✨ Features

| Feature | Description |
|--------|-------------|
| 🎨 **Stunning Dark UI** | Custom CSS with animated gradient accents, glassmorphism, and smooth animations |
| ⚡ **Blazing Fast** | Powered by Groq — the fastest LLM inference available |
| 🧠 **Multi-Model Support** | Switch between Llama 3.3 70B, Mixtral 8x7B, Gemma2, and more |
| 💬 **Full Chat History** | Maintains conversation context across the entire session |
| 🎛 **Custom System Prompts** | Define Nova's personality and behavior on the fly |
| 🌡 **Temperature Control** | Fine-tune creativity vs. precision with a live slider |
| ⚡ **Quick Prompts** | One-click starter prompts to get the conversation going |
| 📊 **Live Stats** | See message counts for you and Nova in real time |
| 💾 **Export Chats** | Download your full conversation as a `.txt` file |
| 🗑 **Clear & Reset** | Wipe the slate clean instantly |
| 🔴 **Live Indicator** | Animated badge shows Nova is always online and ready |
| ⌨️ **Typing Animation** | Bouncing dots while Nova formulates a response |

---

## 🛠 Tech Stack

```
✦ Frontend     →  Streamlit (custom CSS + animations)
🦜 LLM Layer   →  LangChain (ChatGroq, message history)
⚡ Inference   →  Groq API (fastest LLM API on the planet)
🧠 Models      →  Llama 3.3 70B · Llama 3.1 70B · Mixtral 8x7B · Gemma2 9B
🐍 Language    →  Python 3.9+
🎨 Fonts       →  Cabinet Grotesk · Instrument Sans (Google Fonts)
```

---

## 🚀 Quick Start

### 1️⃣ Clone the repo

```bash
git clone https://github.com/yourusername/nova-ai.git
cd nova-ai
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set up your environment

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 🔑 Don't have a Groq API key? Grab one for free at [console.groq.com](https://console.groq.com)

### 4️⃣ Run Nova

```bash
streamlit run app.py
```

🎉 Open your browser at `http://localhost:8501` and start chatting!

---

## 📦 Requirements

```txt
streamlit
langchain
langchain-groq
python-dotenv
```

Or install everything at once:

```bash
pip install streamlit langchain langchain-groq python-dotenv
```

---

## 🎨 UI Highlights

Nova AI features a hand-crafted dark theme with:

- 🌈 **Animated rainbow accent bar** that slides across the top
- 💎 **Pulsing gem logo** with a soft glow effect
- 🌊 **Floating orb** on the empty state screen
- 📨 **Spring-animated message bubbles** that bounce in
- ✍️ **Typing indicator** with staggered dot animation
- 🌟 **Gradient text** on headings that shifts over time
- 🔵 **Glassmorphism-style message bubbles** for AI responses

---

## 🤖 Supported Models

| Model | Context | Best For |
|-------|---------|----------|
| 🦙 `llama-3.3-70b-versatile` | 128k | General use — **recommended** |
| 🦙 `llama-3.1-70b-versatile` | 128k | General use |
| 🌀 `mixtral-8x7b-32768` | 32k | Creative writing, coding |
| 💎 `gemma2-9b-it` | 8k | Fast, lightweight tasks |

---

## 🗂 Project Structure

```
nova-ai/
│
├── 📄 app.py              # Main Streamlit app
├── 📄 .env                # API keys (not committed)
├── 📄 .env.example        # Example env file
├── 📄 requirements.txt    # Python dependencies
└── 📄 README.md           # You are here ✦
```

---

## ⚙️ Configuration

Nova is highly configurable — right from the sidebar:

| Setting | Default | Description |
|---------|---------|-------------|
| 🤖 Model | `llama-3.3-70b-versatile` | The LLM to use |
| 🌡 Temperature | `0.7` | 0 = focused, 1 = creative |
| 📝 System Prompt | Built-in Nova persona | Sets Nova's personality |

---

## 🧹 Tips & Tricks

- 💡 Use **Quick Prompts** to instantly explore Nova's capabilities
- 🎭 Change the **System Prompt** to make Nova a coding assistant, tutor, or creative writer
- 🌡 Lower **temperature** (`0.1–0.3`) for factual, precise answers
- 🎨 Higher **temperature** (`0.8–1.0`) for creative, imaginative responses
- 💾 **Export** your chats before clearing to save important conversations

---

## 🤝 Contributing

Contributions are welcome! 🙌

```bash
# 1. Fork the repo
# 2. Create your feature branch
git checkout -b feature/amazing-feature

# 3. Commit your changes
git commit -m "✨ Add amazing feature"

# 4. Push to the branch
git push origin feature/amazing-feature

# 5. Open a Pull Request 🎉
```

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- ⚡ [Groq](https://groq.com) — for the world's fastest LLM inference
- 🦜 [LangChain](https://langchain.com) — for the elegant LLM abstraction layer
- 🎈 [Streamlit](https://streamlit.io) — for making Python UIs magical
- 🦙 [Meta AI](https://ai.meta.com) — for the Llama model family
- 🌀 [Mistral AI](https://mistral.ai) — for Mixtral

---

<div align="center">

Made with ❤️ and lots of ✦ magic

**⭐ Star this repo if Nova made your day!**

</div>
