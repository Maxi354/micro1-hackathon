🛡️ DevShield AI: Agentic Code Gatekeeper
DevShield is an AI-powered code auditing, repair, and verification pipeline built with Python, Streamlit, and the Google Gemini API.
Unlike standard single-prompt LLM wrappers that output unverified code, DevShield implements an agentic, test-driven self-healing loop. It automatically parses candidate functions, executes flake8 static analysis, generates dynamic ⁠pytest⁠ suites for edge cases, and runs code in an isolated sandbox. If tests fail, DevShield captures the exact execution trace and iteratively patches the function until all edge cases pass.
⚡ Key Features
 Static Code Analysis: Integrates ⁠flake8⁠ to flag syntax issues, unused imports, and style violations prior to test execution.
 Dynamic Pytest Synthesis: Leverages Gemini to automatically engineer targeted ⁠pytest⁠ test suites—covering zero-division, missing dictionary keys, empty inputs, type mismatches, and mock payloads.
 Isolated Sandbox Execution: Runs generated tests in temporary, isolated execution environments with strict process timeouts (preventing infinite loops and memory leaks).
 Iterative Self-Healing Loop: Feeds raw sandbox failure logs and tracebacks back to the agent to dynamically patch code until 100% of test cases pass.
 Streamlit Visual Dashboard: Displays real-time step-by-step execution traces, sandbox logs, execution speed metrics, and side-by-side code diffs.
 Fail-Safe Fallbacks: Robust model fallback handling across Gemini API endpoints to ensure maximum uptime and sub-second verification.
 🏗️ System Architecture & Workflow
 ┌───────────────────────────────┐
               │       User Input Code         │
               └───────────────┬───────────────┘
                               │
                               ▼
               ┌───────────────────────────────┐
               │   1. Static Analysis (flake8) │
               └───────────────┬───────────────┘
                               │
                               ▼
               ┌───────────────────────────────┐
               │ 2. Dynamic Pytest Synthesis   │
               └───────────────┬───────────────┘
                               │
                               ▼
    ┌────────► ┌───────────────────────────────┐
    │          │ 3. Isolated Sandbox Execution │
    │          │           (pytest)            │
    │          └───────────────┬───────────────┘
    │                          │
    │                   Passed or Failed?
    │                   /             \
  FAILED               /               \  PASSED
    │                 ▼                 ▼
┌───┴───────────────┐          ┌───────────────────┐
│ 4. Auto-Repair    │          │  Verified Final   │
│ Feedback Loop     │          │      Code 🎉      │
└───────────────────┘          └───────────────────┘
🛠️ Tech Stack
 Language: Python 3.10+
 Frontend Dashboard: Streamlit
 LLM Engine: Google Gemini API (⁠gemini-1.5-flash⁠, ⁠gemini-1.5-pro⁠)
 Static Analysis: ⁠flake8⁠
 Dynamic Testing Framework: ⁠pytest⁠
 Environment & Config: ⁠python-dotenv⁠, ⁠requests⁠
🎯 Scope & Verification Boundaries
DevShield is designed for standalone Python functions, algorithmic modules, and data transformation utilities.
 ✅ Supported: Pure functions, data parsing (JSON/Dicts), mathematical logic, string formatting, sensor telemetry pipelines, and standard library operations.
 ⚠️ Out of Scope (By Design): GUI apps (Tkinter/PyQt), hardware I/O (Raspberry Pi GPIO), active database network calls, and multi-file internal package imports.
🚀 Reproduction Guide (Setup & Execution)
1. Prerequisites
 Python 3.10+ installed
 A valid Google Gemini API Key
2. Installation
Clone the repository and install dependencies:
git clone https://github.com/Maxi354/micro1-hackathon.git
cd micro1-hackathon
pip install -r requirements.txt
3. Environment Configuration
Create a ⁠.env⁠ file in the root directory:
GEMINI_API_KEY=your_gemini_api_key_here
4. Application Execution
Launch the Streamlit interface:
streamlit run app.py
📂 Project Structure
.
├── agent.py          # Core agentic pipeline (flake8, pytest generator, sandbox runner)
├── app.py            # Streamlit dashboard & live trace visualizer
├── requirements.txt  # Project dependencies
├── .env              # Environment configuration (API keys)
└── README.md         # Project documentation