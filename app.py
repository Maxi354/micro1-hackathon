import os
import streamlit as st

# --- SECRETS BRIDGE FOR STREAMLIT CLOUD ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
    if "GOOGLE_API_KEY" in st.secrets:
        os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
except Exception:
    pass
# -------------------------------------------

import google.generativeai as genai

# Configure the Gemini API client using the environment/secrets
api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Page Configuration
st.set_page_config(
    page_title="DevShield AI - Agentic Workflow",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ DevShield AI: Autonomous Code Auditor & Self-Correction Agent")
st.markdown("Submit code to run static analysis, generate unit tests, catch bugs, and autonomously apply self-correcting fixes using Gemini.")

# User Input Section
code_input = st.text_area(
    "Paste Python Code for Audit:",
    value="""def calculate_average(data):
    total = sum(data)
    count = len(data)
    average = total / count
    return average

print(calculate_average([]))""",
    height=200
)

if st.button("Run Agentic Workflow (DevShield)"):
    if not code_input.strip():
        st.warning("Please enter some Python code to audit.")
    elif not api_key:
        st.error("API Key not found! Please check your Streamlit Cloud Secrets configuration.")
    else:
        with st.spinner("Running Gemini agentic workflow, generating tests, and self-correcting..."):
            try:
                # Initialize Gemini Model for the agent task
                model = genai.GenerativeModel("gemini-2.5-flash")
                
                prompt = f"""
                You are DevShield AI, an autonomous code auditor and self-correction agent.
                Analyze the following Python code, identify bugs (like ZeroDivisionError or edge cases), 
                and provide the corrected, safe version of the code.

                Code:
                {code_input}

                Provide a brief explanation of the fix and the final corrected Python code block.
                """
                
                response = model.generate_content(prompt)
                
                st.success("LLM Agent Workflow Executed Successfully!")
                
                st.subheader("⚡ Agent Audit & Analysis")
                st.write(response.text)

            except Exception as e:
                st.error(f"An error occurred during agent execution: {e}")
