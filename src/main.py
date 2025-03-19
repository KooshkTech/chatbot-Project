from src.graph.chatbot_graph import create_workflow

def main():
    workflow = create_workflow()
    # Start workflow with initial state
    for step in workflow.stream({"start": True}):
        print(f"Step output: {step}")

if __name__ == "__main__":
    main()