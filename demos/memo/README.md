# Memo

A modern spaced repetition quiz application built with Python, featuring both CLI and MCP server interfaces for flexible learning workflows.

# Installation

```bash
# Install Python 3.13 with pyenv
pyenv install 3.13.1
pyenv local 3.13.1

# Install dependencies
uv sync
```

# Usage

```bash
# Review available cards
uv run memo main
uv run memo main --cards 2

# Add new cards
uv run memo add --front "question" --back "answer"
uv run memo add --csv facts.csv

# Start an mcp server to review with your agent
uv run memo mcp
```

# Core Features

**Multiple Interfaces**
CLI for direct use and MCP server for integration with AI assistants

**Local knowledge**

- Cards are saved in SQLite on your computer
- Add new cards through the CLI, MCP, or CSV import

**Spaced Repetition**

- Intelligent scheduling based on your performance and memory retention
- Calculates a nextDate based on your grade:
  - 0: wrong
  - 1: significant effort
  - ...
  - 5: effortless

# MCP Tools

The memo mcp server registers the following tools:

- `get_next_question`: Returns next scheduled question
- `save_score(question_id, grade)`: Update spaced repetition schedule
- `add_card(front, back)`: Adds a single new card
- `import_cards(csv_filepath)`: Bulk import cards from csv

# System design

## Tech Stack

- **Language**: Python 3.13
- **CLI Framework**: Typer for command-line interface
- **Database**: SQLite for persistent storage and progress tracking
- **MCP Framework**: FastMCP for Model Context Protocol server
- **Environment**: pyenv + uv for dependency management
- **Architecture**: Spec-driven development with Tessl

## Project Structure

```bash
memo/
├── specs/
│   ├── cli.spec.md   # CLI interface
│   ├── mcp.spec.md   # MCP server implementation
│   ├── quiz.spec.md  # Core quiz logic
│   ├── srs.spec.md   # Spaced repetition algorithm
│   └── db.spec.md
├── memo/
├── tests/
├── facts.csv         # Seed data
└── pyproject.toml
```

The other files in the repo either are either Tessl configuration files and context or files that were added as part of the video that this repo was created for.

# Next Steps

## Iterate using the Tessl Framework

The project already has a `package.json` which you can use to run the Tessl and connect to it via MCP:

```bash
npm i # this installs both Tessl and Claude
npx tessl login # login to Tessl
npx claude # run Claude which will automatically connect to Tessl via MCP
```

## Connect via MCP

If you update the `.mcp.json` file to the following you can connect to the MCP server from inside Claude:

```json
{
  "mcpServers": {
    "srs": {
      "type": "stdio",
      "command": "uv",
      "args": ["run", "memo", "mcp"]
    },
    "tessl": {
      "type": "stdio",
      "command": "tessl",
      "args": ["mcp"]
    }
  }
}
```
