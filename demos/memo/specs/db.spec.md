# Database Module

Database interface for the memo application. Provides SQLite-based storage for flashcards with spaced repetition system (SRS) data.

## Target

[@generate](../memo/db.py)

## Capabilities

### Database Initialization

Initialize SQLite database and create the cards table with all required fields for SRS functionality.

- Creates database file at 'memo.db' in current directory [@test](../tests/test_db_init.py)
- Creates cards table with proper schema including SRS fields [@test](../tests/test_db_init.py)
- Handles database creation safely (no errors if already exists) [@test](../tests/test_db_init.py)

### Card Management

Create, retrieve, and update individual flashcards with SRS data.

- Create new cards with front/back text and default SRS values [@test](../tests/test_create_card.py)
- Retrieve single cards by ID [@test](../tests/test_get_card.py)
- Retrieving a non-existent card returns None [@test](../tests/test_get_card.py)
- Update card SRS values (repetition, easiness, interval, next_date) [@test](../tests/test_update_card.py)
- Updating a non-existent card returns False [@test](../tests/test_update_card.py)
- Automatically update timestamps on card modifications [@test](../tests/test_update_card.py)
- Retrieve all cards from database [@test](../tests/test_get_all_cards.py)

### Review System Support

Retrieve cards that are due for review based on SRS scheduling.

- Get cards where next_date is today or earlier [@test](../tests/test_get_due_cards.py)
- Order results by next_date (earliest first) [@test](../tests/test_get_due_cards.py)
- Support optional limit on number of cards returned [@test](../tests/test_get_due_cards.py)
- Return all cards when no filtering needed [@test](../tests/test_get_due_cards.py)

### Bulk Operations

Import cards from external sources for efficient data loading.

- Import cards from CSV files with 'front' and 'back' columns [@test](../tests/test_import_from_csv.py)
- Create cards with proper default SRS values during import [@test](../tests/test_import_from_csv.py)
- Handle CSV parsing and validation [@test](../tests/test_import_from_csv.py)
- Returns the number of cards imported [@test](../tests/test_import_from_csv.py)

## API

```python { .api }
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class Card:
    id: int
    front: str
    back: str
    repetition: int = 0
    easiness: float = 2.5
    interval: int = 1
    next_date: str = ""
    created_at: str = ""
    updated_at: str = ""

@dataclass
class Repository:
    db_path: str = "memo.db"

    def init_db(self) -> None:
        """Initialize database and create tables"""
        pass

    def create_card(self, front: str, back: str) -> int:
        """Create new card with default SRS values. Returns card ID."""
        pass

    def get_card(self, card_id: int) -> Optional[Card]:
        """Get single card by ID"""
        pass

    def update_card(self, card_id: int, repetition: int, easiness: float,
                   interval: int, next_date: str) -> bool:
        """Update card's SRS values. Returns True if successful."""
        pass

    def get_due_cards(self, limit: Optional[int] = None) -> List[Card]:
        """Get cards where next_date <= today, ordered by next_date"""
        pass

    def import_from_csv(self, csv_path: str) -> int:
        """Bulk import cards from CSV file. Returns number of cards imported."""
        pass

    def get_all_cards(self) -> List[Card]:
        """Get all cards from database"""
        pass
```

## Tests

### Test Database Setup

All tests use a temporary test database 'test_memo.db' that is created before each test and deleted after each test to ensure isolation.

### Mock Data Setup

#### test_db_init.py
- Start with no database file
- Verify database and table creation from scratch

#### test_create_card.py
- Start with empty database (no cards)
- Test data: front="Hello", back="Hola"

#### test_get_card.py
- Pre-populate with sample cards:
  - Card 1: front="Cat", back="Gato", id=1
  - Card 2: front="Dog", back="Perro", id=2
  - Card 3: front="House", back="Casa", id=3

#### test_update_card.py
- Pre-populate with 2 cards with specific SRS values:
  - Card 1: id=1, repetition=1, easiness=2.5, interval=1, next_date="2024-01-15"
  - Card 2: id=2, repetition=3, easiness=2.8, interval=7, next_date="2024-01-20"

#### test_get_due_cards.py
- Pre-populate with cards having different next_dates:
  - Card 1: next_date="2024-01-10" (past due)
  - Card 2: next_date="2024-01-15" (due today, assuming test runs on 2024-01-15)
  - Card 3: next_date="2024-01-20" (future)
  - Card 4: next_date="2024-01-25" (future)

#### test_import_from_csv.py
- Create test CSV file 'test_cards.csv' with sample data:
  ```
  front,back
  Apple,Manzana
  Book,Libro
  Water,Agua
  ```
- Start with empty database

#### test_get_all_cards.py
- Pre-populate with 4 cards:
  - Card 1: front="Red", back="Rojo"
  - Card 2: front="Blue", back="Azul"
  - Card 3: front="Green", back="Verde"
  - Card 4: front="Yellow", back="Amarillo"

## Dependencies

### SQLite Database

Uses Python's built-in sqlite3 module for database operations.  
[@use](sqlite3)

### Date Handling

Uses Python's datetime module for timestamp and date string management.  
[@use](datetime)

### CSV Processing

Uses Python's csv module for parsing CSV files during import operations.  
[@use](csv)