import streamlit as st
from agent import diagnose
from evaluator import verify
from logger import log_interaction
from tests import run_tests

st.set_page_config(page_title="Circuit Debug AI", layout="centered")

st.title("⚡ Circuit Debugging AI Assistant")
st.write("Diagnose and troubleshoot circuit problems using AI with verification.")

# Sidebar
st.sidebar.title("⚙️ Options")
show_logs = st.sidebar.checkbox("Show Logs")

# Input
user_input = st.text_area("Describe your circuit issue:", height=150)

if st.button("Analyze Circuit"):
    if user_input.strip() == "":
        st.warning("Please enter a circuit issue.")
    else:
        with st.spinner("Analyzing..."):
            diagnosis = diagnose(user_input)
            evaluation, confidence = verify(user_input, diagnosis)

            log_interaction(user_input, diagnosis, evaluation, confidence)

        st.success("Analysis Complete")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔍 Diagnosis")
            st.write(diagnosis)

        with col2:
            st.subheader("🧪 Verification")
            st.write(evaluation)

        st.subheader("📊 Confidence")
        st.write(confidence)

# Show logs
if show_logs:
    try:
        with open("log.txt", "r") as f:
            st.text(f.read())
    except:
        st.write("No logs yet.")

st.markdown("---")

# Test button
if st.button("Run System Tests"):
    results, passed, total = run_tests()

    st.subheader("🧪 Test Results")

    for r in results:
        if r["passed"]:
            st.success(f"{r['input']} → Passed ({r['confidence']})")
        else:
            st.error(f"{r['input']} → Failed ({r['confidence']})")

    st.write(f"### {passed}/{total} tests passed")
