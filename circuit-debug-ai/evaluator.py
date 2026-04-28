import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

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

    response = model.generate_content(prompt)

    result = response.text

    confidence = "Unknown"
    for line in result.split("\n"):
        if "Confidence" in line:
            confidence = line.strip()

    return result, confidence
