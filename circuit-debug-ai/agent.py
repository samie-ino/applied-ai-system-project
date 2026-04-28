import google.generativeai as genai
import os
from dotenv import load_dotenv
from retriever import retrieve_context

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def diagnose(problem):
    context = retrieve_context(problem)

    prompt = f"""
You are a specialized electrical engineering assistant.

Follow this process:
1. Think step-by-step about the problem
2. Use retrieved context if relevant
3. Generate:
   - Possible causes
   - Suggested tests

Context:
{context}

Problem:
{problem}
"""

    response = model.generate_content(prompt)

    return response.text
