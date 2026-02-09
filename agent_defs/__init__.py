from agents import Agent
from services.tools import read_code_file, analyze_code, code_review

base_reviewer = Agent(
    name="Code Reviewer",
    instructions="Analyze the given code. Use analyze_code, code_review, read_code_file for feedback.",
    tools=[read_code_file, analyze_code, code_review],
    model="gpt-4o-mini",
)

code_cop = base_reviewer.clone(name="Code Cop", instructions="Strict reviewer. Point out every deviation. Do not sugarcoat feedback.")
pirate_debugger = base_reviewer.clone(name="Pirate Debugger", instructions="Speak in pirate lingo. Still give useful insights.")
poetic_reviewer = base_reviewer.clone(name="Poetic Reviewer", instructions="Give feedback in rhyming couplets. Ensure advice remains useful.")

persona_names = {"base": "Code Reviewer", "cop": "Code Cop", "pirate": "Pirate Debugger", "poet": "Poetic Reviewer"}
agent_map = {"base": base_reviewer, "cop": code_cop, "pirate": pirate_debugger, "poet": poetic_reviewer}
