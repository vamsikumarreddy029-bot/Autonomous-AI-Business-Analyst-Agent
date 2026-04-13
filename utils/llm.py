from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic


def get_llm(provider, api_key):

    if provider == "OpenAI":
        return ChatOpenAI(
            api_key=api_key,
            model="gpt-4o-mini",
            temperature=0
        )

    elif provider == "Gemini":
        return ChatGoogleGenerativeAI(
            google_api_key=api_key,
            model="gemini-pro",
            temperature=0
        )

    elif provider == "Claude":
        return ChatAnthropic(
            api_key=api_key,
            model="claude-3-sonnet-20240229",
            temperature=0
        )

    else:
        raise ValueError("Invalid provider")