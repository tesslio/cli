# Plan: Create Memo CLI Quiz Tool

Build a simple CLI quiz tool called "memo" using Python and Typer framework.

## Tasks

- [x] Bootstrap project with Python/Typer configuration using uv and pyenv
  > **Bash** `pyenv local 3.13.2`
  > Set Python version for project
  > 
  > ---
  > 
  > **Bash** `uv init --no-workspace`
  > Initialized uv project structure
  > 
  > ---
  > 
  > **Bash** `mkdir -p specs memo tests`
  > Created project directories
  > 
  > ---
  > 
  > **Edit** `pyproject.toml`
  > - Updated project metadata and dependencies
  > - Added Typer and Rich as dependencies
  > - Configured CLI entry point
  > - Added setuptools package configuration
  > 
  > ---
  > 
  > **Write** [`memo/__init__.py`](../memo/__init__.py)
  > Created package init file with version
  > 
  > ---
  > 
  > **Bash** `uv sync`
  > Installed project dependencies
  > 
  > ---
  > 
  > **Bash** `uv pip install -e .`
  > Installed memo package in editable mode
  > 
  > ---
  > 
  > **Bash** `uv add --dev pytest pytest-cov`
  > Added testing dependencies
  > 
  > ---
  > 
  > **Edit** [`AGENTS.md`](../AGENTS.md)
  > Documented project configuration including:
  > - Python 3.13.2 with pyenv + uv
  > - Typer CLI framework
  > - pytest testing framework
  > - Directory structure (specs, memo, tests)
  > - Development commands

- [x] Interview user for quiz requirements.
  > User requirements gathered:
  > - Load questions from facts.csv file
  > - Run through all questions sequentially
  > - Compare user answers to correct answers
  > - Print final score at the end
  > - No need to persist results
- [x] Create spec for memo CLI tool
  > **MCP** `tessl - create`
  > - spec: specs/cli.spec.md
  > - prompt: CLI quiz tool with CSV loading, interactive quiz, scoring
  > 
  > Created [specs/cli.spec.md](../specs/cli.spec.md)
  > User reviewed and approved spec

- [x] Build initial implementation from spec
  > **MCP** `tessl - build`
  > - spec: ["specs/cli.spec.md"]
  > 
  > Generated [memo/cli.py](../memo/cli.py)
  > Build partially succeeded, code was generated
  > 
  > ---
  > 
  > **Edit** `memo/cli.py`
  > - Updated CSV column names from "question"/"answer" to "front"/"back" to match existing facts.csv
  > 
  > Adjusted to match existing CSV format

- [x] Test the CLI tool
  > **Bash** `uv run memo --help`
  > CLI help command works correctly, showing usage and options