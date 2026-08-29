1.# DevShield AI: Agentic Code Gatekeeper

DevShield AI is an automated code auditing, test generation, and self-correcting feedback loop system powered by Python and Google's Gemini models. It provides deep static analysis (via flake8), automated unit test generation (via pytest), and agentic sandboxed runtime validation to keep your codebase secure and robust.

---

## Features

- **Automated Code Auditing:** Scans submitted Python code for style, syntax, and logic issues.
- **Agentic Pipeline (`agent.py`):** Core orchestration handling iterative test generation, execution, and feedback loops.
- **Interactive Live Dashboard (`app.py`):** A clean Streamlit interface allowing developers to run both baseline single-prompt fixes and full multi-step agentic workflows.

---

## Reproduction Guide

Follow these steps to run DevShield AI locally from a clean environment:

### 1. Clone the Repository
```bash
git clone [https://github.com/Maxi354/micro1-hackathon.git](https://github.com/Maxi354/micro1-hackathon.git)
cd micro1-hackathon

2. Create and Activate a Virtual Environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
Create a ⁠.env⁠ file in the root directory and add your Google Gemini API key:
GOOGLE_API_KEY=your_actual_api_key_here
(Note: If deploying to Streamlit Community Cloud, add this key under your app's Secrets settings instead).

5. Run the Application
streamlit run app.py

Improvement Changelog
 Initial Implementation: Built the core agentic pipeline (⁠agent.py⁠) integrating static analysis checks and automated test generation scripts.
 UI Streamlining: Developed a responsive Streamlit dashboard (⁠app.py⁠) with side-by-side execution options for baseline single-prompt fixes versus full agentic workflows.
 Robust Security & Deployment: Configured ignore rules and environment handling to protect credentials while ensuring seamless cloud deployment.
