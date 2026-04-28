from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def verify(problem, diagnosis):
    prompt = f"""
You are an evaluator.

Check if the diagnosis is correct and consistent.

Problem:
{problem}

Diagnosis:
{diagnosis}

Return:
- Issues (if any)
- Confidence: X%
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    confidence = "Unknown"
    for line in result.split("\n"):
        if "Confidence" in line:
            confidence = line.strip()

    return result, confidence
