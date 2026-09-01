from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode
from langfuse.langchain import CallbackHandler

from perfectionist.states import GraphState
from perfectionist.nodes.constructor import constructor_node
from perfectionist.nodes.querier import querier_node

def build_graph():
    builder = StateGraph(GraphState)

    # builder.add_node('constructor', constructor_node)
    builder.add_node('querier', querier_node)
    
    # builder.add_edge(START, 'constructor')
    # builder.add_edge('constructor', END)
    builder.add_edge(START, 'querier')
    builder.add_edge('querier', END)

    langfuse_handler = CallbackHandler()
    return builder.compile().with_config({"callbacks": [langfuse_handler]})


graph = build_graph()