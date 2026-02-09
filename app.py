"""Multi-Persona AI Code Review - Streamlit App. Run with: streamlit run app.py"""

import asyncio
import streamlit as st
from agents import Runner, set_default_openai_key

from config import get_config
from agent_defs import agent_map, persona_names
from utils.logging import get_logger

logger = get_logger(__name__)

st.set_page_config(page_title="AI Code Review Personas", layout="wide")
st.title("Multi-Persona AI Code Review System")

try:
    cfg = get_config()
    set_default_openai_key(cfg["openai_api_key"])
except ValueError as e:
    st.error(str(e))
    st.stop()

# Persona selector with descriptions
PERSONA_DESCRIPTIONS = {
    "base": "Balanced code analysis using tools for feedback.",
    "cop": "Strict reviewer. Points out every deviation; no sugarcoating.",
    "pirate": "Useful insights delivered in pirate lingo.",
    "poet": "Feedback in rhyming couplets while keeping advice practical.",
}
agent_key = st.sidebar.selectbox(
    "Choose Persona",
    list(persona_names.keys()),
    format_func=lambda k: persona_names[k],
)
current_agent = agent_map[str(agent_key)]
with st.sidebar.expander("Persona descriptions"):
    for k, label in persona_names.items():
        st.caption(f"**{label}** — {PERSONA_DESCRIPTIONS.get(k, '')}")

if "last_output" not in st.session_state:
    st.session_state.last_output = ""
if "code_input" not in st.session_state:
    st.session_state.code_input = ""

# Code input section
st.markdown("### Paste your code")
code_input = st.text_area(
    "Paste your code here",
    height=150,
    value=st.session_state.code_input,
    placeholder="Paste code (Python, JS, Java, C/C++, Go, etc.) or use the file upload below.",
)
st.markdown("#### Or upload a code file")
uploaded_file = st.file_uploader("Upload a file", type=["py", "txt", "js", "java", "cpp", "c", "go", "md", "json"])

with st.expander("Example snippet"):
    st.code("def hello():\n    print('Hello, World!')\n    return 42", language="python")

col1, col2 = st.columns([1, 1])
with col1:
    send = st.button("Send for Review")
with col2:
    reset = st.button("Reset")

if reset:
    st.session_state.last_output = ""
    st.session_state.code_input = ""
    st.rerun()

user_code = code_input
if uploaded_file:
    try:
        user_code = uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error(f"Error reading file: {e}")
        user_code = None

if send:
    if not user_code or not str(user_code).strip():
        st.warning("Please paste code or upload a file.")
    else:
        st.session_state.code_input = code_input
        with st.spinner("Reviewing code..."):
            try:
                result = asyncio.run(Runner.run(current_agent, user_code))
                st.session_state.last_output = result.final_output
                logger.info("Code review completed")
            except Exception as e:
                st.session_state.last_output = f"Error: {e}"
                logger.exception("Code review failed")
        st.rerun()

if st.session_state.last_output:
    st.markdown("---")
    with st.expander("Review Output", expanded=True):
        st.markdown(st.session_state.last_output)
