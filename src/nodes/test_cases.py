from src.utils.groq_utils import generate_with_groq

def generate_test_cases(state):
    """Generate test cases from code"""
    prompt = f"Generate test cases for: {state['code']}"
    return {"test_cases": generate_with_groq(prompt)}