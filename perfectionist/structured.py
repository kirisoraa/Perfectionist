from pydantic import BaseModel, Field

class QuerierStructuredAnswer(BaseModel):
    queries: list[str] = Field(description="List")