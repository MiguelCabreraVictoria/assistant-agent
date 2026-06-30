from graph.assistant.builder import build_graph
from graph.assistant.state import AssistantState


def main():
    graph = build_graph()

    state = AssistantState(
        messages=["Agenda un cita a las 7 am"]
    )

    result = graph.invoke(state)

    print("=== RESULT ===")
    print(result["response"])
    print(result["intent"])
    print(result["execution"])


if __name__ == "__main__":
    main()