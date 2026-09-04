from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langgraph.graph import END
from ddgs import DDGS

from ..states import GraphState

def search_node(state: GraphState) -> dict:
    search = DDGS()
    queries = state['current_queries']
    search_results = []
    grabbed_links = []
    for query in queries:
        result = search.text(query, max_results=5, safesearch="off", timelimit="y", page=1, backend="auto")
        print(result)
        for search_result in result:
            if search_result['href'] not in grabbed_links:
                search_results.append(search_result)
                grabbed_links.append(search_result['href'])

    return {'search_results': search_results}
    