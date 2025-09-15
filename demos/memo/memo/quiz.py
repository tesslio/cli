# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/quiz.spec.md
# (spec:8decc358) (code:b0d0fdc0)

from typing import List, Tuple, Optional
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from memo.db import Repository, Card
from memo.srs import sm2

console = Console()

def load_due_cards(repo: Repository, limit: Optional[int] = None) -> List[Card]:
    """Load due cards from database. Optional limit on number of cards."""
    return repo.get_due_cards(limit)

def run_quiz(repo: Repository, cards: List[Card]) -> Tuple[int, int]:
    """Run interactive SRS quiz with given cards. Returns (reviewed_count, total_count)."""
    if not cards:
        console.print("[red]No cards available for quiz![/red]")
        return (0, 0)
    
    console.print(Panel(
        f"[bold blue]Quiz Started![/bold blue]\n"
        f"Total Cards: {len(cards)}\n"
        f"Type your answers and press Enter",
        title="Quiz Instructions",
        border_style="blue"
    ))
    
    reviewed = 0
    total = len(cards)
    
    for i, card in enumerate(cards, 1):
        console.print(f"\n[bold]Card {i}/{total}[/bold]")
        
        # Display question in a panel
        question_panel = Panel(
            card.front,
            title=f"Question {i}",
            border_style="cyan"
        )
        console.print(question_panel)
        
        # Get user answer
        user_answer = Prompt.ask("Your answer").strip()
        
        # Grade the answer
        grade = grade_answer(user_answer, card.back)
        
        # Provide feedback
        if grade == 5:
            console.print("[green]✓ Correct![/green]")
        else:
            console.print(f"[red]✗ Incorrect. The correct answer was: {card.back}[/red]")
        
        # Calculate new SRS values
        item_data = {
            'repetition': card.repetition,
            'easiness': card.easiness,
            'interval': card.interval
        }
        
        srs_result = sm2(item_data, grade)
        
        # Update card in database
        next_date_str = srs_result['next_date'].isoformat()
        repo.update_card(
            card.id,
            srs_result['repetition'],
            srs_result['easiness'],
            srs_result['interval'],
            next_date_str
        )
        
        reviewed += 1
    
    # Display final results
    console.print(Panel(
        f"[bold]Quiz Complete![/bold]\n\n"
        f"Cards Reviewed: [green]{reviewed}/{total}[/green]\n"
        f"Great work! 🎉",
        title="Quiz Results",
        border_style="green"
    ))
    
    return (reviewed, total)

def grade_answer(user_answer: str, correct_answer: str) -> int:
    """Grade user answer compared to correct answer. Returns grade 0-5."""
    # Exact match (case-insensitive): grade 5
    if user_answer.strip().lower() == correct_answer.strip().lower():
        return 5
    # Wrong answer: grade 0
    else:
        return 0
