from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode
from langfuse.langchain import CallbackHandler

from perfectionist.states import GraphState
from perfectionist.nodes.querier import querier_node
from perfectionist.nodes.search import search_node
from perfectionist.nodes.fetch import fetch_node
from perfectionist.nodes.summarizer import summarizer_node

def build_graph():
    builder = StateGraph(GraphState)

    # builder.add_node('constructor', constructor_node)
    builder.add_node('querier', querier_node)
    builder.add_node('search', search_node)
    builder.add_node('fetch', fetch_node)
    builder.add_node('summarizer', summarizer_node)
    
    # builder.add_edge(START, 'constructor')
    # builder.add_edge('constructor', END)
    builder.add_edge(START, 'querier')
    builder.add_edge('querier', 'search')
    builder.add_edge('search', 'fetch')
    builder.add_edge('fetch', 'summarizer')
    builder.add_edge('summarizer', END)

    langfuse_handler = CallbackHandler()
    return builder.compile().with_config({"callbacks": [langfuse_handler]})


graph = build_graph()