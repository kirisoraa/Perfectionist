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
            search_results[i]['content'] = content
            fetch_results.append(search_results[i])
        


    # return search_results

    return {'messages': '\n###########################\n'.join(i['content'] for i in fetch_results)}