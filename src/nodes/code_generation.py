from src.utils.groq_utils import generate_with_groq

def generate_code(state: dict) -> dict:
    """
    Generate code based on design documents.
    Args:
        state (dict): The current state of the workflow.
    Returns:
        dict: Updated state with generated code.
    """
    if "design_docs" in state:
        prompt = f"Generate code for the following design documents: {state['design_docs']}"
        state["code"] = generate_with_groq(prompt)
    else:
        state["code"] = "No design documents available to generate code."
    return state