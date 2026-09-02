from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langgraph.graph import END
from langchain_community.tools import DuckDuckGoSearchResults

from ..states import GraphState

def search_node(state: GraphState) -> dict:
    search = DuckDuckGoSearchResults(num_results=5)
    queries = state['current_queries']
    search_results = []
    grabbed_links = []
    for query in queries:
        result = search.run(query)
        for search_result in result:
            if search_result['link'] not in grabbed_links:
                search_results.append(search_result)
                grabbed_links.append(search_result['link'])

    