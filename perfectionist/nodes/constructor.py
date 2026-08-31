from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langgraph.graph import END

from ..states import GraphState
from ..llm import get_llm

CONSTRUCTOR_SYSTEM_PROMPT = """
You are given a Master Query. Your task is to analyze the Master Query and understand what questions need to be answered in order to answer the Master Query.

# TASK STEPS
1. Analyze the Master Query. Gain an understanding of what and why needs to be researched and answered to result in a perfect answer to the Master Query.
2. Using your understanding, break down the Master Query into anywhere from 1 to 5 sub-questions. These sub-questions must encompass the whole master query together, but each be a single, focused task, and have minimal overlap between each other.

# OUTPUT FORMAT
A new-line delimited, non-numbered list of sub-questions. 
Each subquestion must be on a new line and start with * as a delimiter.
Prefer concise, concrete, focused questions to overlapping and lengthy ones.

# Master Query
""".strip()

def constructor_node(state: GraphState) -> dict:
    llm = get_llm()
    user_query = state['messages'][-1].content
    context = [SystemMessage(content=CONSTRUCTOR_SYSTEM_PROMPT+'\n'+user_query)]

    response = llm.invoke(context)

    print("CONSTRUCTOR OUT:", response)
    return {"messages": [response]}

