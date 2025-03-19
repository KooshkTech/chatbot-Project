from src.utils.groq_utils import generate_with_groq

def create_design_docs(state: dict) -> dict:
    """
    Generate design documents from user stories.
    Args:
        state (dict): The current state of the workflow.
    Returns:
        dict: Updated state with design documents.
    """
    if "user_stories" in state:
        prompt = f"Create design documents for the following user stories: {state['user_stories']}"
        state["design_docs"] = generate_with_groq(prompt)
    else:
        state["design_docs"] = "No user stories available to generate design documents."
    return state