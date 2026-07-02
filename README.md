<h1 align="center">🚀 ML From Scratch To Pro</h1>
<h3 align="center">A day-by-day journey through Machine Learning — from NumPy basics to production-ready ML, Deep Learning & LLM-powered systems</h3>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&color=1DA1F2&center=true&vCenter=true&width=600&lines=Learning+ML+one+day+at+a+time+%F0%9F%93%88;NumPy+%E2%86%92+Pandas+%E2%86%92+EDA+%E2%86%92+Streamlit+%E2%86%92+LLM+Chatbots;Documenting+every+step+publicly+%F0%9F%93%9D" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Yaqoob-hassan/ML-From-Scratch-To-Pro?style=for-the-badge&color=yellow" />
  <img src="https://img.shields.io/github/forks/Yaqoob-hassan/ML-From-Scratch-To-Pro?style=for-the-badge&color=blue" />
  <img src="https://img.shields.io/github/last-commit/Yaqoob-hassan/ML-From-Scratch-To-Pro?style=for-the-badge&color=green" />
</p>

---

## 📖 About This Repository

This repo is my **public learning log** — a structured, day-by-day record of my journey through Machine Learning, Deep Learning, and now **LLM-powered application development**.

Every day = one topic. Every folder = working code + notes explaining *what* I learned and *why* it matters. The goal isn't just to collect scripts — it's to build a repository that shows the **full pipeline of a modern ML skillset**:

> **Data handling → Analysis → Visualization → Deployment → AI/LLM Integration**

That means someone browsing this repo can see how raw data becomes a clean DataFrame, how that DataFrame becomes an interactive dashboard, and how those same Python fundamentals extend into building AI chatbots on top of LLM APIs like Gemini.

---

## 🗺️ Roadmap

| Day | Topic | Folder | Status |
|-----|-------|--------|--------|
| 01 | NumPy Basics | [`Day01_NumPy`](./Day01_NumPy) | ✅ Done |
| 02 | NumPy Indexing, Slicing & Filtering | [`Day02_NumPy`](./Day02_NumPy) | ✅ Done |
| 03 | Pandas Basics (IRIS Dataset) | [`Day03_Pandas`](./Day03_Pandas) | ✅ Done |
| 04 | Data Preprocessing & EDA | [`Day04_Preprocessing`](./Day04_Preprocessing) | ✅ Done |
| 05 | Interactive Dashboards with Streamlit | [`Day05_Streamlit`](./Day05_Streamlit) | ✅ Done |
| 06 | **LLM Chatbots with Gemini API** | [`Day06_LLM_Chatbots`](./Day06_LLM_Chatbots) | 🆕 New |
| 07+ | Deep Learning, ML Deployment & More | `Day07_...` | 🔜 Upcoming |

---

## 🤖 Day 06 — LLM Chatbots (New!)

The newest addition to this journey — moving from *training models on data* to *building applications on top of pretrained LLMs*.

This section covers how to build conversational AI apps using Google's **Gemini API**, focused on core engineering concepts rather than just "calling an API":

- 🧠 **Stateless API design** — why the full conversation history must be resent every call, and how to manage that state locally
- 💬 **Message roles** (`user` vs `model`) and why mislabeling them breaks conversational flow
- 📦 **Multi-part message structure** — why `parts` is a list of dicts, built to support text + images + files
- 🔐 **Secrets management** — using `.env` + `load_dotenv()` instead of hardcoding API keys
- ⚡ **Streamlit caching** — `st.cache_data` vs `st.cache_resource`, and why using the wrong one on a DataFrame is dangerous
- 🖥️ Building an interactive chatbot UI with Streamlit, wired up to the Gemini API

```
Day06_LLM_Chatbots/
├── README.md
├── 01_basic_gemini_chatbot/
│   ├── chatbot.py
│   ├── .env.example
│   └── notes.md
├── 02_customer_support_bot/      🔜
├── 03_study_buddy_bot/           🔜
└── requirements.txt
```

Each sub-folder here is a themed chatbot — connecting the **data + dashboard skills** from earlier days with **LLM API integration**, so the same Streamlit skills from Day 05 now power an AI-driven interface instead of just a data dashboard.

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,numpy,pandas,streamlit,git,github,vscode" />
</p>

---

## 📂 Repository Structure

```
ML-From-Scratch-To-Pro/
├── Day01_NumPy/
├── Day02_NumPy/
├── Day03_Pandas/
├── Day04_Preprocessing/
├── Day05_Streamlit/
├── Day06_LLM_Chatbots/          👈 New
│   └── 01_basic_gemini_chatbot/
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Use This Repo

```bash
# Clone the repository
git clone https://github.com/Yaqoob-hassan/ML-From-Scratch-To-Pro.git
cd ML-From-Scratch-To-Pro

# Install dependencies
pip install -r requirements.txt

# For the chatbot, set up your own API key
cd Day06_LLM_Chatbots/01_basic_gemini_chatbot
cp .env.example .env   # then add your own Gemini API key inside
python chatbot.py
```

---

## 🎯 Why This Repo Exists

> *"Discipline is the difference between what you want now and what you want most."* — inspired by the mindset of staying consistent, one day at a time.

This isn't about finishing fast — it's about **showing up daily** and documenting the process honestly, including the bugs, the confusion, and the fixes. If you're learning ML too, feel free to follow along, fork it, or reach out.

---

## 🔗 Connect With Me

<p align="left">
  <a href="https://github.com/Yaqoob-hassan"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/muhammad-yaqoob-hassan"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
</p>

---

<p align="center">⭐ If this repo helps you on your own ML journey, consider giving it a star!</p>
