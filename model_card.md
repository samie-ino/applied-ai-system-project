## 🧪 Reliability & Testing

To ensure the system works reliably and not just superficially, the following methods were implemented:

- **Confidence Scoring:**  
  The AI evaluator assigns a confidence score (0–100%) based on how consistent and reasonable the diagnosis is.

- **Self-Verification (Agentic Check):**  
  A second AI pass reviews the original diagnosis to detect contradictions or errors.

- **Logging:**  
  All inputs, generated outputs, and verification results are recorded locally for debugging and traceability.

- **Human Evaluation:**  
  Outputs were manually reviewed to confirm whether suggested causes and tests were realistic and useful.

### Testing Results

- 5 out of 6 test cases produced accurate and relevant troubleshooting steps  
- The system struggled when user input lacked detail or context  
- Confidence scores averaged **~0.86**, with higher scores correlating to clearer inputs  
- Verification reduced incorrect or misleading responses compared to a single-pass system  

### Key Insight
Adding a verification step significantly improved reliability, showing that structured AI workflows are more effective than relying on a single generated response.


## ⚠️ Responsible AI Reflection

### Limitations & Biases
This system relies on a general-purpose language model, which means its responses are based on learned patterns rather than true understanding. As a result, it can sometimes produce overly generic or incomplete diagnoses, especially when user input lacks detail. The system is also biased toward common circuit problems, meaning it may not perform as well on highly specialized or uncommon scenarios.

### Potential Misuse & Prevention
The AI could be misused if users rely on it as a definitive authority for critical engineering decisions without verification. To reduce this risk, the system includes a verification step, confidence scoring, and encourages users to test suggestions rather than blindly trust them. Additionally, it avoids presenting outputs as guaranteed solutions and instead frames them as possible causes and steps.

### What Surprised Me
One surprising result during testing was how much the quality of the input affected the output. When the input was clear and specific, the AI performed very well and produced accurate troubleshooting steps. However, vague inputs led to weaker and more generalized responses, highlighting the importance of context in AI systems.

### Collaboration with AI
Throughout this project, I used AI as a collaborator rather than a decision-maker.

- **Helpful instance:**  
  AI was effective at quickly generating structured troubleshooting steps and organizing them into clear categories (causes, tests, verification), which helped speed up development.

- **Flawed instance:**  
  In some cases, the AI produced confident but overly generic explanations that did not fully address the specific problem. This reinforced the need to verify outputs and not assume correctness based on how confident the response sounded.

Overall, this project showed me that AI is most useful when guided, checked, and integrated into a structured system rather than used independently.
