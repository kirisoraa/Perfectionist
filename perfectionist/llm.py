from langchain_openai import ChatOpenAI

def get_llm(nothink=False):
    base_url = 'http://llm:26278/v1'
    api_key='-'
    model = 'perfectionist-llm'

    if nothink:
        return ChatOpenAI(
            base_url = base_url,
            api_key=api_key,
            model = model,
            model_kwargs={
                "extra_body": {
                    "chat_template_kwargs": {
                        "enable_thinking": False,
                    }
                }
            },
        )
    else:
        return ChatOpenAI(
            base_url = base_url,
            api_key=api_key,
            model = model
        )