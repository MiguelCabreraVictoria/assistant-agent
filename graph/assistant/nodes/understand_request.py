from graph.assistant.state import AssistantState

def understand_request(state: AssistantState) -> AssistantState:
    """
    Analyze the user message and determine 
    wich capacity should manage
    """
    if not state.messages:
        state.intent = "conversation"
        return state
    
    message = state.messages[-1].lower()

    if "gasto" in message or "ingreso" in message:
        state.intent = "finance"
    elif "recuerdame" in message or "tarea" in message:
        state.intent = "productivity"
    elif "agenda" in message or "evento" in message:
        state.intent = "calendar"

    elif "salud" in message:
        state.intent = "health"

    elif "familia" in message:
        state.intent = "family"

    else:
        state.intent = "conversation"

    return state
