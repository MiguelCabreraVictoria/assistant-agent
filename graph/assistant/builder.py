from langgraph.graph import StateGraph, START, END

from graph.assistant.state import AssistantState
from graph.assistant.router import router
from graph.assistant.nodes import (
    understand_request,
    build_response,
)


def build_graph():
    graph = StateGraph(AssistantState)

    graph.add_node("understand_request", understand_request)
    graph.add_node("build_response", build_response)

    graph.add_edge(START, "understand_request")

    graph.add_conditional_edges(
        "understand_request",
        router,
        {
            "conversation": "build_response",
            "productivity": "build_response",
            "finance": "build_response",
            "calendar": "build_response",
            "health": "build_response",
            "family": "build_response",
        },
    )

    graph.add_edge("build_response", END)

    return graph.compile()