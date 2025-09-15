# Memo CLI

Command-line interface for the memo spaced repetition system. Provides commands to review cards, add new cards, and run the MCP server.

## Usage

The CLI provides three main commands for managing spaced repetition cards:

### Review Cards (Default Command)

```bash
# Review all available cards
memo

# Review a limited number of cards
memo --cards 10
```

### Add Cards

```bash
# Add a single card
memo add --front "What is Python?" --back "A programming language"

# Import cards from CSV file
memo add --csv cards.csv
```

### Run MCP Server

```bash
# Start the MCP server for external tool access
memo mcp
```

## Target

[@generate](../memo/cli.py)

## Capabilities

### Main command for reviewing cards

Default command that reviews available cards from the database.

- Initialize database on first run if needed
- Optional --cards parameter to limit number of cards reviewed (default: no limit)
- Load due cards from database using Repository
- Run interactive quiz with loaded cards
- Display quiz results showing cards reviewed

### Add command for creating cards

Subcommand for adding new cards to the database with two modes.

Single card mode:
- Uses --front and --back parameters to create individual cards
- Validates that both front and back are provided
- Creates card in database using Repository
- Shows success message

CSV import mode:
- Uses --csv parameter with path to CSV file
- Imports cards from CSV using Repository.import_from_csv
- Shows success message with count of imported cards

Both modes initialize database if needed.

### MCP server command

Command to run the MCP server for external tool access.

- Imports create_mcp_server from memo.mcp_server module
- Uses asyncio to run the server asynchronously
- Includes proper error handling

## API

```python { .api }
import typer
import asyncio
from rich.console import Console
from pathlib import Path
from typing import Optional
from memo.db import Repository
from memo.quiz import run_quiz
from memo.mcp_server import create_mcp_server

app = typer.Typer()
console = Console()

@app.command()
def main(cards: Optional[int] = typer.Option(None, help="Limit number of cards to review")) -> None:
    """Review available cards (default command)."""
    pass

@app.command()
def add(
    front: Optional[str] = typer.Option(None, help="Front side of the card"),
    back: Optional[str] = typer.Option(None, help="Back side of the card"),
    csv: Optional[Path] = typer.Option(None, help="Path to CSV file to import")
) -> None:
    """Add new cards to the database."""
    pass

@app.command()
def mcp() -> None:
    """Run the MCP server."""
    pass

if __name__ == "__main__":
    app()
```

## Dependencies

### Typer
CLI framework for building the command-line interface.
[@use](typer)

### Rich
Terminal formatting and user interface components.
[@use](rich)

### Pathlib
Built-in Python module for file path operations.
[@use](pathlib)

### Asyncio
Built-in Python module for asynchronous programming.
[@use](asyncio)

### Database Module
Repository class for database operations and card management.
[@use](./db.spec.md)

### Quiz Module
Quiz functionality for running interactive quizzes.
[@use](./quiz.spec.md)

### MCP Server Module
MCP server functionality for creating and running the server.
[@use](./mcp_server.spec.md)