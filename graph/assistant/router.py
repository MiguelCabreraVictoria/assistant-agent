from graph.assistant.state import AssistantState
from models.model_loader import get_ollama_llm
from observability.langfuse_client import get_langfuse_handler
from prompts.registry import prompt_registry
from prompts.prompts import PromptName

llm = get_ollama_llm()

def router(state: AssistantState):
    message = state.messages[-1] if state.messages else ""

    handler = get_langfuse_handler()

    system_prompt = prompt_registry.get(
        name=PromptName.INTENT_CLASSIFIER,
        label="production"
    )


    messages = [
        ("system", system_prompt),
        ("user", message),
    ]

    response = llm.invoke(
        messages,
        config={"callbacks": [handler]}
    )

    intent = response.content.strip().lower()

    state.intent = intent
    state.execution.current_graph = intent

    return intent