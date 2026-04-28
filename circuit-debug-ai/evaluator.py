from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def verify(problem, diagnosis):
    prompt = f"""
You are verifying an AI-generated circuit diagnosis.

Problem:
{problem}

Diagnosis:
{diagnosis}

Check:
- Is it logically consistent?
- Are there errors?

Return:
Verification summary
Confidence score (0-100%)
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    # simple confidence extraction
    confidence = "Unknown"
    for line in result.split("\n"):
        if "%" in line:
            confidence = line.strip()

    return result, confidence
