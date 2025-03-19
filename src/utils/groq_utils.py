import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def get_groq_client():
    """Initialize Groq client"""
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_with_groq(prompt):
    """Generate content using Groq API"""
    client = get_groq_client()
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",  # Use Groq's Mixtral model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content