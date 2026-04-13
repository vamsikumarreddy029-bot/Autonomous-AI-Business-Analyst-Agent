def plan_task(user_query, llm):

    prompt = f"""
Classify the task into ONE word:

Query: {user_query}

Options:
- general
- strategy
- data

Return only one word.
"""

    return llm.invoke(prompt).content.strip().lower()