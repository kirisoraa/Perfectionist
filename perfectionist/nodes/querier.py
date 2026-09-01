from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langgraph.graph import END

from ..states import GraphState
from ..llm import get_llm

QUERIER_SYSTEM_PROMPT = """
You are given a Question. Your task is to construct a web search query that is the most likely to produce results that answer the Question.

# TASK STEPS
1. Analyze the Question and think how best to search for answers to the Question.
2. Write one or two web search queries that will get passed to a web search tool.

# OUTPUT FORMAT
A new-line delimited, non-numbered list of queries. 
Each query must be on a new line and start with * as a delimiter.
Prefer concise and focused keywords to semantically correct sentences.
Make sure the queries overlap as little as possible, only write more than one if necessary.

# The Question
""".strip()


def querier_node(state: GraphState) -> dict:
    llm = get_llm(nothink=True)
    user_query = state['messages'][-1].content
    context = [SystemMessage(content=QUERIER_SYSTEM_PROMPT+'\n'+user_query)]

    response = llm.invoke(context)

    print("QUERIER OUT:", response)
    return {"messages": [response]}