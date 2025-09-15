# Project

# Tessl & Spec Driven Development <!-- tessl-managed -->

This project uses the [Tessl spec driven development framework](.tessl/framework/agents.md) and toolkit for software development: @.tessl/framework/agents.md

# Knowledge Index <!-- tessl-managed -->

Documentation for dependencies and processes can be found in the [Knowledge Index](./KNOWLEDGE.md)

# Plan Files <!-- tessl-managed -->

ALWAYS create [plan files](.tessl/framework/plan-files.md) when planning: @.tessl/framework/plan-files.md

## Project Configuration

### Stack
- **Language**: Python 3.13.2
- **Environment Management**: pyenv + uv
- **CLI Framework**: Typer with Rich for formatting
- **Testing Framework**: pytest with pytest-cov

### Directory Structure
- **Specs**: `./specs` - Tessl specifications
- **Source Code**: `./memo` - Main application code
- **Tests**: `./tests` - Test files

### Development Commands
- **Install Dependencies**: `uv sync`
- **Install Package (editable)**: `uv pip install -e .`
- **Run Tests**: `uv run pytest`
- **Run Tests with Coverage**: `uv run pytest --cov=memo`
- **Run CLI**: `uv run memo`