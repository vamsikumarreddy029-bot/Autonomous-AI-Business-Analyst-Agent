# 🧠 Autonomous AI Business Analyst Agent

🚀 Live Demo: https://autonomous-ai-business-analyst-agent-tyfqdvduqsnp9oewrkaebp.streamlit.app/
📂 GitHub: https://github.com/vamsikumarreddy029-bot/Autonomous-AI-Business-Analyst-Agent

---

## 🌐 Overview

An **Autonomous AI Agent** that performs **business analysis, strategy generation, and data-driven decision-making**.

Unlike traditional AI systems:

* ❌ Chatbots → Just answer
* ❌ RAG → Retrieve + respond

✅ This system:

* Understands the problem
* Decides what to do
* Uses tools
* Generates actionable insights

---

## 🎯 Key Capabilities

### 🧠 Intelligent Task Classification

Automatically detects:

* General queries
* Business strategy problems
* Data analysis tasks

---

### ⚙️ Tool-Based Execution System

* 📊 Data Analysis (Pandas)
* 📈 Visualization (Plotly)
* 🔮 Forecasting (ML - Linear Regression)

---

### 💡 Insight Generation Engine

Provides:

* Key insights
* Root causes
* Actionable recommendations

---

### 🤖 Multi-LLM Support

* OpenAI (GPT-4o-mini)
* Google Gemini (1.5 Flash)
* Anthropic Claude (Sonnet)

---

## 🏗️ Architecture

```
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

```
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
```

---

## ⚙️ Installation

```bash
git clone https://github.com/vamsikumarreddy029-bot/Autonomous-AI-Business-Analyst-Agent
cd Autonomous-AI-Business-Analyst-Agent

pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 💡 Example Use Cases

### 📊 Data Analysis

Upload CSV → Ask:

> “Why did revenue drop?”

→ Output:

* Trends 📈
* Forecast 🔮
* Insights 💡

---

### 📈 Business Strategy

> “How to scale my startup?”

→ Output:

* Growth strategy
* Step-by-step plan
* Recommendations

---

### 💬 General AI

> “Explain customer churn”

→ Structured explanation

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

> “I built an autonomous AI agent that performs multi-step reasoning, dynamically routes tasks, integrates analytical tools, and generates actionable business insights using multi-LLM support.”

---

## 🚀 Future Enhancements

* 🧠 Memory (conversation history)
* 🤖 Multi-agent collaboration
* 📊 Advanced forecasting (Prophet)
* 📄 Multi-file support (PDF, Excel)

---

## 👨‍💻 Author

**Vamsi Kumar Reddy**
AI / ML Engineer

---

⭐ If you found this useful, give it a star!
