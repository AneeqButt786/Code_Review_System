# # Multi-Persona AI Code Review System

## Overview

An AI-powered code review system with selectable personas (strict, poetic, pirate, etc.). It analyzes code for best practices, bugs, and style, delivering feedback in various tones to suit user preferences.

## Features

- Multiple personas: Code Reviewer, Code Cop, Pirate Debugger, Poetic Reviewer
- Code analysis tools: code_review, analyze_code, read_code_file
- Streamlit UI with persona selector and file upload
- Real-time review output

## Tech Stack

- Python 3.12+, OpenAI Agents SDK, Streamlit, python-dotenv

## Setup

1. `cd Code_Review_System`
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and set `OPENAI_API_KEY`

## Run Commands

```bash
streamlit run app.py
```

## Example Use Cases

1. Paste a Python script and select "Code Cop" for strict feedback
2. Upload a JS file and select "Pirate Debugger" for whimsical review
3. Paste code and select "Poetic Reviewer" for lyrical feedback

## Folder Structure

```
Code_Review_System/
├── app.py
├── config.py
├── agent_defs/__init__.py
├── services/__init__.py, tools.py
├── utils/__init__.py, config.py, logging.py
├── .env.example, README.md, requirements.txt
```
