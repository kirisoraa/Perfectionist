from typing import Optional, TypedDict, Annotated
from pydantic import BaseModel, Field
from langgraph.graph import MessagesState


class GraphState(MessagesState):
    master_query: str
    open_questions: list[str]
    answered_questions: dict[str,str]
    iteration_budget: int
    