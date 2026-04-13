import streamlit as st

from utils.llm import get_llm
from agent.planner import plan_task
from agent.executer import execute
from agent.insights import generate_insights

st.set_page_config(page_title="AI Agent", layout="wide")

st.title("🧠 Autonomous AI Business Analyst Agent")

# Sidebar
with st.sidebar:
    provider = st.selectbox("LLM", ["OpenAI", "Gemini", "Claude"])
    api_key = st.text_input("API Key", type="password")

# Upload CSV
file = st.file_uploader("Upload CSV", type=["csv"])

query = st.text_input("Ask business question")

if st.button("Run Agent"):

    if not api_key:
        st.warning("Enter API key")
        st.stop()

    if not file or not query:
        st.warning("Upload file and enter query")
        st.stop()

    try:
        llm = get_llm(provider, api_key)

        # PLAN
        plan = plan_task(query, llm)
        st.subheader("🧠 Plan")
        st.write(plan)

        # EXECUTE
        data_summary = execute(file)
        st.subheader("📊 Data Analysis")
        st.json(data_summary)

        # INSIGHTS
        insights = generate_insights(data_summary, query, llm)
        st.subheader("🚀 Insights")
        st.write(insights)

    except Exception as e:
        st.error(str(e))