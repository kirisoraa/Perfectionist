from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langgraph.graph import END

from ..states import GraphState
from ..llm import get_llm

SUMMARIZER_SYSTEM_PROMPT = """
You are given a Question, and the results of a web search. 
Your task is to answer the Question as accurately as possible using the given results of the web search.
Prioritize accuracy and truth above all else. If you do not know something, say so. If the web search is not enough, then do not invent or hallucinate information - acknowledge the gap.

# The Question
{question}

-----------------
WEB SEARCH RESULTS START BELOW
-----------------
{web_search_context}
""".strip()


def summarizer_node(state: GraphState) -> dict:
    llm = get_llm()
    user_query = state['master_query']

    web_search_context = ''

    search_results = state['search_results']
    for search_result in search_results:
        web_search_context += '# ' + search_result['title'] + '\n\n' + search_result['content'] + '\n\n\n'

    context = [SystemMessage(content=SUMMARIZER_SYSTEM_PROMPT.format(question=user_query, web_search_context=web_search_context))]

    response = llm.invoke(context)

    print("SUMMARIZER OUT:", response)
    return {
        "messages": response
    }