"""Tool functions for Code Review System."""

from agents import function_tool


@function_tool
def code_review(code: str) -> str:
    """Performs quick code analysis and returns high-level feedback."""
    issues = []
    if "eval(" in code:
        issues.append("Avoid using eval() - it's a security risk.")
    if "import *" in code:
        issues.append("Avoid import * - it pollutes the namespace.")
    if "print(" in code:
        issues.append("Consider using logging instead of print statements.")
    return "\n".join(issues) if issues else "No major issues detected."


@function_tool
def analyze_code(code: str) -> str:
    """Analyzes the code and returns mock feedback."""
    if "while True" in code:
        return "Infinite loop detected: while True without a break!"
    if "class" in code and "def" in code:
        return "Class structure detected. Consider checking for SRP (Single Responsibility Principle)."
    return "Code looks clean!"


@function_tool
def read_code_file(filepath: str) -> str:
    """Reads a code file and returns its content."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"
