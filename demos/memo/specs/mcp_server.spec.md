# MCP Server

MCP server module that provides tools for accessing and managing flashcards through the Model Context Protocol.

## Target

[@generate](../memo/mcp_server.py)

## Capabilities

### Provides get_next_question tool

Returns the next due card from the database for review.

- Initializes database if needed
- Gets the next due card from database with limit 1
- Returns dict with question_id (card id), front (question), and back (answer)
- If no cards due, returns appropriate message indicating no cards available

### Provides save_score tool

Processes quiz results and updates card SRS values.

- Takes question_id (card id) and grade (0-5) as parameters
- Retrieves card from database using question_id
- Uses sm2 algorithm to calculate new SRS values based on grade
- Updates card in database with new repetition, easiness, interval, and next_date
- Returns success message with next review date

### Provides add_card tool

Creates new flashcards in the database.

- Takes front (question) and back (answer) text as parameters
- Creates new card in database using Repository.create_card
- Returns card id and success message

### Provides import_cards tool

Bulk imports flashcards from CSV files.

- Takes csv_filepath parameter
- Uses Repository.import_from_csv to process the file
- Returns count of successfully imported cards

### Initializes MCP server

Sets up FastMCP server with all required tools registered.

- Creates server instance with proper configuration
- Registers all four tools with appropriate schemas
- Handles server startup and tool execution

## API

```python { .api }
from fastmcp import FastMCP
from typing import Dict, Any

def create_mcp_server() -> FastMCP:
    """Create and configure the MCP server with all tools."""
    pass

async def get_next_question() -> Dict[str, Any]:
    """Get the next due card for review.
    
    Returns:
        Dict containing 'question_id', 'front', 'back' or message if no cards due
    """
    pass

async def save_score(question_id: int, grade: int) -> Dict[str, Any]:
    """Save quiz score and update card SRS values.
    
    Args:
        question_id: Card ID from database
        grade: Grade from 0-5
        
    Returns:
        Dict with success message and next review date
    """
    pass

async def add_card(front: str, back: str) -> Dict[str, Any]:
    """Add new flashcard to database.
    
    Args:
        front: Question text
        back: Answer text
        
    Returns:
        Dict with card_id and success message
    """
    pass

async def import_cards(csv_filepath: str) -> Dict[str, Any]:
    """Import cards from CSV file.
    
    Args:
        csv_filepath: Path to CSV file with 'front' and 'back' columns
        
    Returns:
        Dict with count of imported cards
    """
    pass

if __name__ == "__main__":
    # Server startup code
    pass
```

## Dependencies

### Database Module

Repository and Card classes for database operations and card management.
[@use](./db.spec.md)

### SRS Module

SM-2 algorithm implementation for calculating spaced repetition values.
[@use](./srs.spec.md)

### FastMCP

MCP server implementation framework for creating tools and handling requests.
[@use](fastmcp)