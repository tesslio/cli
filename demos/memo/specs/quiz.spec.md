# Quiz Module

Handles all quiz-related functionality including loading due cards from database and running interactive SRS quizzes.

## API

```python { .api }
from typing import List, Tuple, Optional
from memo.db import Repository, Card

def load_due_cards(repo: Repository, limit: Optional[int] = None) -> List[Card]:
    """Load due cards from database. Optional limit on number of cards."""
    pass

def run_quiz(repo: Repository, cards: List[Card]) -> Tuple[int, int]:
    """Run interactive SRS quiz with given cards. Returns (reviewed_count, total_count)."""
    pass

def grade_answer(user_answer: str, correct_answer: str) -> int:
    """Grade user answer compared to correct answer. Returns grade 0-5."""
    pass
```

## Target

[@generate](../memo/quiz.py)

## Capabilities

### Load due cards from database

Loads due cards from the database using the Repository.

- Uses Repository to get due cards from database where next_date <= today
- Takes optional limit parameter for number of cards
- Returns list of Card objects that are due for review
- Card objects contain id, front (question), back (answer), and SRS fields: repetition, easiness, interval, next_date

### Run interactive SRS quizzes

Runs interactive quiz sessions with spaced repetition system integration.

Quiz flow:
- Load due cards where next_date <= today
- For each card, display front (question) and get user answer
- Grade the answer (5 for correct, 0 for wrong)
- Calculate new SRS values using sm2(card_dict, grade) where card_dict contains current SRS values
- Update card in database with new repetition, easiness, interval, next_date from sm2 results
- Show feedback after each answer (correct/incorrect)
- Track and return review counts as (number_reviewed, total_cards_shown)

### Grade answers

Compares user answers to correct answers and assigns grades.

- Exact match (case-insensitive): grade 5
- Wrong answer: grade 0
- Returns integer grade for SRS algorithm

### Display quiz interface

Creates rich formatted displays for quiz presentation.

- Uses Rich panels for question display
- Shows progress and results with proper styling
- Displays feedback after each answer

## Dependencies

### Database Module

Repository and Card classes for database operations. Card objects contain id, front, back, and SRS fields (repetition, easiness, interval, next_date).
[@use](./db.spec.md)

### SRS Module

SM-2 algorithm implementation for spaced repetition calculations. The sm2 function takes a dict with SRS values and returns updated values including next_date.
[@use](./srs.spec.md)

### Rich Console and Components

Rich library components for console output, user prompts, and panel displays.
[@use](rich)