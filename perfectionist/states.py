from typing import Optional, TypedDict, Annotated
from pydantic import BaseModel, Field
from langgraph.graph import MessagesState


class GraphState(MessagesState):
    master_query: str
    current_queries: list[str]
