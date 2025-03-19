def product_owner_review(state: dict) -> dict:
    """
    Simulate product owner review process.
    Args:
        state (dict): The current state of the workflow.
    Returns:
        dict: Updated state with review results.
    """
    if "user_stories" in state:
        # Simulate approval based on story length and content
        story_length = len(state["user_stories"])
        contains_keywords = any(keyword in state["user_stories"].lower() for keyword in ["user", "want", "so that"])
        
        state["approved"] = story_length > 100 and contains_keywords
        state["feedback"] = (
            "Stories are too short or missing key elements. Please add more details."
            if not state["approved"]
            else "Approved! Stories are detailed and well-structured."
        )
    else:
        state["approved"] = False
        state["feedback"] = "No user stories to review."
    return state