# 🧠 Autonomous AI Business Analyst Agent

🚀 A multi-capability AI agent that performs **business analysis, strategy generation, and data-driven insights** using tool-based execution and multi-LLM support.

---

## 🌐 Overview

This project is a **decision-making AI system** — not just a chatbot.

Unlike traditional systems:

* ❌ RAG → retrieves answers
* ❌ Chatbot → responds to queries

✅ This system:

* Analyzes problems
* Chooses actions
* Uses tools
* Generates **insights + strategies**

---

## 🎯 Key Features

### 🧠 Intelligent Task Routing

* Automatically classifies user queries into:

  * General Question
  * Business Strategy
  * Data Analysis

---

### ⚙️ Tool-Based Execution

* 📊 Data Analysis (Pandas)
* 📈 Chart Generation (Plotly)
* 🔮 Forecasting (Machine Learning)

---

### 💡 Insight Generation

* Produces:

  * Key insights
  * Root causes
  * Actionable recommendations

---

### 🤖 Multi-LLM Support

* OpenAI (GPT-4o-mini)
* Gemini (Google)
* Claude (Anthropic)

---

## 🏗️ Architecture

```text
User Input
   ↓
Planner Agent 🧠
   ↓
Task Routing
   ↓
Tool Execution ⚙️
   ↓
Insight Generator 💡
   ↓
Final Output 🚀
```

---

## 📁 Project Structure

```text
ai-business-agent/
│
├── app.py
├── requirements.txt
│
├── agent/
│   ├── planner.py
│   ├── executer.py
│   ├── insights.py
│
├── tools/
│   ├── data_tool.py
│   ├── chart_tool.py
│   ├── forecast_tool.py
│
├── utils/
│   └── llm.py
│
└── data/
```

---

## ⚙️ Installation

```bash
git clone <your-repo-link>
cd ai-business-agent

pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔑 API Keys

You can use any of the following:

* OpenAI → https://platform.openai.com/api-keys
* Gemini → https://makersuite.google.com/app/apikey
* Claude → https://console.anthropic.com

---

## 💡 Example Use Cases

### 📊 Data Analysis

> Upload CSV → Ask: “Why did sales drop?”

→ Generates:

* Trends
* Forecast
* Insights

---

### 📈 Business Strategy

> “How to grow my startup?”

→ Returns:

* Strategy
* Steps
* Recommendations

---

### 💬 General Queries

> “Explain marketing funnel”

→ Provides structured explanation

---

## 🔥 Tech Stack

* Python
* Streamlit
* LangChain
* OpenAI / Gemini / Claude
* Pandas / NumPy
* Plotly
* Scikit-learn

---

## 🎯 Interview Pitch

> “I built an autonomous AI agent that performs multi-step reasoning, dynamically routes tasks, integrates tools for data analysis and forecasting, and generates actionable business insights using multi-LLM support.”

---

## 🚀 Future Improvements

* 🧠 Memory (conversation history)
* 🤖 Multi-agent collaboration
* 📊 Advanced forecasting (Prophet)
* 🧾 File support (PDF, Excel)

---

## 📌 Author

**Vamsi Kumar Reddy**
AI Engineer | Machine Learning Enthusiast

---

⭐ If you like this project, give it a star!
