from langchain_openai import ChatOpenAI

def get_llm(
    base_url: str = 'http://llm:26278/v1',
    model: str = 'perfectionist-llm',
    # temperature: float = 0.2,
    # max_tokens: int = 15000
):
    return ChatOpenAI(
        base_url = base_url,
        api_key='-',
        model = model,
        # temperature = temperature,
        # max_tokens = max_tokens
    )