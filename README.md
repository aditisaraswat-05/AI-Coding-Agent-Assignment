# AI Coding Agent

## Overview

This project is a Python-based AI Coding Agent that understands an existing codebase, creates an implementation plan from a high-level product request, generates code using an LLM, validates the generated output, and updates the target repository automatically.

The target application used for this assignment is:

https://github.com/callicoder/node-easy-notes-app

The product request given to the agent was:

> Improve the application so users can better organise and search their notes.

Instead of manually editing files, the agent analyses the repository, identifies the important files, generates the required code changes, validates them, and writes the updated files back into the repository.

---

# Project Structure

```
AI-Coding-Agent-Assignment
│
├── agent
│   ├── explorer.py
│   ├── planner.py
│   ├── modifier.py
│   ├── validator.py
│   ├── summary.py
│   ├── main.py
│   ├── prompts.py
│   ├── utils.py
│   ├── .env
│   └── generated/
│
├── target-repo/
│
└── README.md
```

---

# Architecture

The project is divided into small independent modules.

### Repository Explorer

Responsible for understanding the repository.

It:

- scans the project
- ignores unnecessary folders
- lists available files
- reads source files
- writes updated code back to the repository
- stores generated copies for reference

---

### Planner

The Planner communicates with the language model.

It receives:

- the user request
- repository file list

and produces a short execution plan describing how the feature should be implemented.

Example:

```
1. Update Note schema
2. Modify controller
3. Update routes
4. Verify existing functionality
```

---

### Modifier

The Modifier generates the actual implementation.

For every selected source file it sends:

- user request
- execution plan
- filename
- original source code

to the LLM.

The response contains the complete updated file.

---

### Validator

The Validator performs a basic validation before saving the generated code.

Currently it checks:

- empty output
- invalid responses
- basic syntax sanity

This helps prevent accidental writes of incomplete responses.

---

### Summary

The Summary module keeps track of modified files and prints the final execution report after the workflow completes.

Example:

```
Modified Files

✔ app/models/note.model.js
✔ app/controllers/note.controller.js
✔ app/routes/note.routes.js
```

---

# Workflow

The overall workflow is straightforward.

```
User Request

        │

        ▼

Repository Explorer

        │

        ▼

Planner

        │

        ▼

Modifier

        │

        ▼

Validator

        │

        ▼

Update Repository

        │

        ▼

Summary
```

---

# Repository Exploration

The repository is explored recursively using Python's `pathlib` module.

Ignored directories include:

- node_modules
- .git
- venv
- __pycache__

Only project source files are considered during analysis.

---

# Assumptions

Some assumptions were made while implementing the agent.

- Only relevant application files need modification.
- Existing functionality should remain unchanged.
- The LLM returns complete source files.
- Generated code is trusted after basic validation.

---

# Trade-offs

A few design decisions were intentionally kept simple.

- Relevant files are selected based on the repository structure rather than analysing every file in detail.
- Validation is lightweight instead of performing full AST parsing.
- The agent updates source files directly after successful generation.

These choices keep the implementation small while still satisfying the assignment requirements.

---

# How to Run

### Clone the repository

```bash
git clone <repository-url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment

Create a `.env` file inside the `agent` folder.

Example:

```
OPENROUTER_API_KEY=your_api_key
```

### Run

```bash
cd agent

python main.py
```

---

# Example Output

```
Repository scanned successfully.

Execution Plan Generated.

Processing app/models/note.model.js

Processing app/controllers/note.controller.js

Processing app/routes/note.routes.js

Repository updated successfully.

Workflow Completed Successfully.
```

---

# Technologies Used

- Python 3.11+
- OpenRouter API
- OpenAI Python SDK
- pathlib
- python-dotenv

---

# Future Improvements

There are several improvements that could be added in future versions.

- Automatically detect relevant files instead of using a predefined list.
- Support repositories written in multiple languages.
- Add syntax validation for different programming languages.
- Generate Git patches instead of directly overwriting files.
- Support rollback if validation fails.
- Add unit testing before updating the repository.

---

# Notes

The goal of this project was to build a simple but extensible AI Coding Agent capable of understanding an existing repository and implementing a feature request with minimal user input while preserving the original application behaviour.