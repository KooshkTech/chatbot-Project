def get_user_requirements(state: dict) -> dict:
    """Collect and process user input requirements"""
    if "user_input" in state:  # Use input from Streamlit
        state["requirements"] = state["user_input"]
    else:
        state["requirements"] = "sample requirements"  # Fallback
    return state

def validate_input(state: dict) -> dict:
    """Validate user input meets minimum criteria"""
    if "requirements" in state:
        # Example validation: Check if requirements are at least 10 characters long
        state["validated"] = len(state["requirements"]) >= 10
        if not state["validated"]:
            state["feedback"] = "Requirements must be at least 10 characters long."
    else:
        state["validated"] = False
        state["feedback"] = "No requirements provided."
    return state