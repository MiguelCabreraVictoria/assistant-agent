from pydantic import BaseModel, Field

class ExecutionState(BaseModel):
    current_graph: str = "assistant"
    current_node: str = "start"


class AssistantState(BaseModel):
    messages: list = Field(default_factory=list)
    intent: str | None = None
    execution: ExecutionState = Field(default_factory=ExecutionState)
    response: str | None = None