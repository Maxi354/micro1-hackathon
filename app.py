import streamlit as st
from agent import run_baseline_fix, run_devshield_agent

st.set_page_config(
    page_title="DevShield AI: Agentic Code Gatekeeper",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ DevShield AI: Agentic Code Gatekeeper")
st.markdown("**Automated code auditing, test generation, and self-correcting feedback loops.**")

# Input Section
input_code = st.text_area(
    "Paste Python Code for Audit:",
    height=240,
    placeholder="def my_function(data):\n    return data[0] / len(data)"
)

col1, col2 = st.columns(2)

with col1:
    btn_baseline = st.button("Run Baseline Fix (Single Prompt)", use_container_width=True)

with col2:
    btn_agent = st.button("Run Agentic Workflow (DevShield)", type="primary", use_container_width=True)

st.divider()

# Baseline Execution
if btn_baseline:
    if not input_code.strip():
        st.warning("Please paste some Python code first!")
    else:
        st.subheader("⚡ Baseline Output (Single Prompt)")
        with st.spinner("Generating single-prompt fix..."):
            baseline_result = run_baseline_fix(input_code)
            st.code(baseline_result, language="python")

# Agentic DevShield Execution
if btn_agent:
    if not input_code.strip():
        st.warning("Please paste some Python code first!")
    else:
        st.subheader("🤖 DevShield Agentic Pipeline")
        with st.spinner("Auditing code, generating test suite, and executing sandbox loops..."):
            results = run_devshield_agent(input_code)
            
            # Display Trajectory Logs in Expanders
            for item in results["trace"]:
                with st.expander(f"📍 Stage: {item['stage']}", expanded=True):
                    st.code(item["result"], language="python" if "Pytest" in item["stage"] else "text")

            st.divider()

            if results["success"]:
                st.success("✅ Code passed all sandbox edge-case verifications!")
            else:
                st.error("⚠️ Maximum retries reached. Check the trace log above for remaining issues.")

            st.subheader("⚡ Verified Final Code")
            st.code(results["final_code"], language="python")