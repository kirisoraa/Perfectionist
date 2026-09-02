from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langgraph.graph import END

from ..structured import QuerierStructuredAnswer
from ..states import GraphState
from ..llm import get_llm

QUERIER_SYSTEM_PROMPT = """
You are given a Question. Your task is to construct a web search query that is the most likely to produce results that answer the Question.

# TASK STEPS
1. Analyze the Question and think how best to search for answers to the Question.
2. Write 1-3 web search queries that will get passed to a web search tool.

# OUTPUT FORMAT
A list of queries, each in separate strings.
Prefer concise and focused keywords to semantically correct sentences.
Make sure the queries overlap semantically as little as possible, only write more than one if necessary.

# The Question
""".strip()


def querier_node(state: GraphState) -> dict:
    llm = get_llm(nothink=True).with_structured_output(QuerierStructuredAnswer)
    user_query = state['master_query']
    context = [SystemMessage(content=QUERIER_SYSTEM_PROMPT+'\n'+user_query)]

    response = llm.invoke(context)

    print("QUERIER OUT:", response)
    return {
        "current_queries": response.queries,
        "messages": ", ".join(response.queries)
    }