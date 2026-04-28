def format_output(user_input, diagnosis, evaluation, confidence):
    return f"""
══════════════════════════════════
🔍 CIRCUIT DEBUG REPORT
══════════════════════════════════

📥 Input:
{user_input}

──────────────────────────────────
⚠️ Diagnosis:
{diagnosis}

──────────────────────────────────
🧠 Verification:
{evaluation}

──────────────────────────────────
📊 Confidence:
{confidence}

══════════════════════════════════
"""
