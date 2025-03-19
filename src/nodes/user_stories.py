from src.utils.groq_utils import generate_with_groq

def generate_user_stories(state):
    """Generate user stories from requirements"""
    prompt = f"Generate user stories for: {state['requirements']}"
    return {"user_stories": generate_with_groq(prompt)}

def revise_stories(state):
    """Revise user stories based on feedback"""
    prompt = f"Revise stories {state['user_stories']} with feedback {state['feedback']}"
    return {"user_stories": generate_with_groq(prompt)}