from openai import OpenAI
import os
from dotenv import load_dotenv
from retriever import retrieve_context

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
