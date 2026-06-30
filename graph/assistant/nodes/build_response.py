from graph.assistant.state import AssistantState

def build_response(state: AssistantState) -> AssistantState:
    state.response = (
        f"Intent: {state.intent}\n"
        f"Current Graph: {state.execution.current_graph}"
    )

    return state