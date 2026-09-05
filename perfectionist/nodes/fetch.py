from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langgraph.graph import END
from trafilatura import fetch_url, extract

from ..states import GraphState

def fetch_node(state: GraphState) -> dict:
    search_results = state['search_results']

    fetch_results = []

    for i, search_result in enumerate(search_results):
        link = search_result['href']
        content = extract(fetch_url(link), output_format="markdown", with_metadata=True)
        if content:
            res = search_results[i]
            res['content'] = content
            fetch_results.append(res)
        


    return {'search_results': fetch_results}
