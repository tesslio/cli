# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/cli.spec.md
# (spec:88299936) (code:1cf5121a)

import typer
import asyncio
from rich.console import Console
from pathlib import Path
from typing import Optional
from memo.db import Repository
from memo.quiz import load_due_cards, run_quiz
from memo.mcp_server import create_mcp_server

app = typer.Typer()
console = Console()

@app.command()
def main(cards: Optional[int] = typer.Option(None, help="Limit number of cards to review")) -> None:
    """Review available cards (default command)."""
    try:
        # Initialize repository and database
        repo = Repository()
        repo.init_db()
        
        # Load due cards from database
        due_cards = load_due_cards(repo, limit=cards)
        
        if not due_cards:
            console.print("[yellow]No cards are due for review![/yellow]")
            return
        
        # Run interactive quiz with loaded cards
        reviewed_count, total_count = run_quiz(repo, due_cards)
        
        # Display results
        console.print(f"[green]Quiz completed! Reviewed {reviewed_count}/{total_count} cards.[/green]")
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)

@app.command()
def add(
    front: Optional[str] = typer.Option(None, help="Front side of the card"),
    back: Optional[str] = typer.Option(None, help="Back side of the card"),
    csv: Optional[Path] = typer.Option(None, help="Path to CSV file to import")
) -> None:
    """Add new cards to the database."""
    try:
        # Initialize repository and database
        repo = Repository()
        repo.init_db()
        
        # CSV import mode
        if csv is not None:
            if not csv.exists():
                console.print(f"[bold red]Error:[/bold red] CSV file '{csv}' not found.")
                raise typer.Exit(code=1)
            
            count = repo.import_from_csv(str(csv))
            console.print(f"[green]Successfully imported {count} cards from {csv}![/green]")
            return
        
        # Single card mode
        if front is not None and back is not None:
            card_id = repo.create_card(front, back)
            console.print(f"[green]Successfully created card #{card_id}![/green]")
            return
        
        # Neither mode specified properly
        if front is None and back is None:
            console.print("[bold red]Error:[/bold red] Please provide either --csv for bulk import or both --front and --back for single card.")
        elif front is None:
            console.print("[bold red]Error:[/bold red] Missing --front parameter.")
        else:
            console.print("[bold red]Error:[/bold red] Missing --back parameter.")
        
        raise typer.Exit(code=1)
        
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        raise typer.Exit(code=1)

@app.command()
def mcp() -> None:
    """Run the MCP server."""
    try:
        server = create_mcp_server()
        # Run the MCP server asynchronously
        asyncio.run(server.run())
    except Exception as e:
        console.print(f"[bold red]Error starting MCP server:[/bold red] {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
