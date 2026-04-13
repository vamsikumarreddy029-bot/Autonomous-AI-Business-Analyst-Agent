def generate_insights(data_summary, user_query, llm):

    prompt = f"""
You are a senior business analyst.

Data:
{data_summary}

Question:
{user_query}

Give:
- Key insights
- Reasons
- Actionable recommendations
"""

    return llm.invoke(prompt).content