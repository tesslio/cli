# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/mcp_server.spec.md
# (spec:adc0969d) (code:c786bd21)

from fastmcp import FastMCP
from typing import Dict, Any
from .db import Repository
from .srs import sm2


def create_mcp_server() -> FastMCP:
    """Create and configure the MCP server with all tools."""
    # Create MCP server
    mcp = FastMCP("Memo Quiz Server")
    
    # Initialize repository
    repo = Repository()
    repo.init_db()
    
    @mcp.tool()
    async def get_next_question() -> Dict[str, Any]:
        """Get the next due card for review.
        
        Returns:
            Dict containing 'question_id', 'front', 'back' or message if no cards due
        """
        due_cards = repo.get_due_cards(limit=1)
        
        if not due_cards:
            return {"message": "No cards are due for review"}
        
        card = due_cards[0]
        return {
            "question_id": card.id,
            "front": card.front,
            "back": card.back
        }
    
    @mcp.tool()
    async def save_score(question_id: int, grade: int) -> Dict[str, Any]:
        """Save quiz score and update card SRS values.
        
        Args:
            question_id: Card ID from database
            grade: Grade from 0-5
            
        Returns:
            Dict with success message and next review date
        """
        card = repo.get_card(question_id)
        if not card:
            return {"error": f"Card with ID {question_id} not found"}
        
        # Prepare current SRS values for sm2 algorithm
        current_values = {
            'repetition': card.repetition,
            'easiness': card.easiness,
            'interval': card.interval
        }
        
        # Calculate new SRS values
        new_values = sm2(current_values, grade)
        
        # Update card in database
        success = repo.update_card(
            question_id,
            new_values['repetition'],
            new_values['easiness'],
            new_values['interval'],
            new_values['next_date'].isoformat()
        )
        
        if success:
            return {
                "message": "Score saved successfully",
                "next_review_date": new_values['next_date'].isoformat()
            }
        else:
            return {"error": "Failed to update card"}
    
    @mcp.tool()
    async def add_card(front: str, back: str) -> Dict[str, Any]:
        """Add new flashcard to database.
        
        Args:
            front: Question text
            back: Answer text
            
        Returns:
            Dict with card_id and success message
        """
        card_id = repo.create_card(front, back)
        return {
            "card_id": card_id,
            "message": "Card added successfully"
        }
    
    @mcp.tool()
    async def import_cards(csv_filepath: str) -> Dict[str, Any]:
        """Import cards from CSV file.
        
        Args:
            csv_filepath: Path to CSV file with 'front' and 'back' columns
            
        Returns:
            Dict with count of imported cards
        """
        try:
            count = repo.import_from_csv(csv_filepath)
            return {
                "count": count,
                "message": f"Successfully imported {count} cards"
            }
        except Exception as e:
            return {"error": f"Failed to import cards: {str(e)}"}
    
    return mcp


async def get_next_question() -> Dict[str, Any]:
    """Get the next due card for review.
    
    Returns:
        Dict containing 'question_id', 'front', 'back' or message if no cards due
    """
    repo = Repository()
    repo.init_db()
    
    due_cards = repo.get_due_cards(limit=1)
    
    if not due_cards:
        return {"message": "No cards are due for review"}
    
    card = due_cards[0]
    return {
        "question_id": card.id,
        "front": card.front,
        "back": card.back
    }


async def save_score(question_id: int, grade: int) -> Dict[str, Any]:
    """Save quiz score and update card SRS values.
    
    Args:
        question_id: Card ID from database
        grade: Grade from 0-5
        
    Returns:
        Dict with success message and next review date
    """
    repo = Repository()
    card = repo.get_card(question_id)
    if not card:
        return {"error": f"Card with ID {question_id} not found"}
    
    # Prepare current SRS values for sm2 algorithm
    current_values = {
        'repetition': card.repetition,
        'easiness': card.easiness,
        'interval': card.interval
    }
    
    # Calculate new SRS values
    new_values = sm2(current_values, grade)
    
    # Update card in database
    success = repo.update_card(
        question_id,
        new_values['repetition'],
        new_values['easiness'],
        new_values['interval'],
        new_values['next_date'].isoformat()
    )
    
    if success:
        return {
            "message": "Score saved successfully",
            "next_review_date": new_values['next_date'].isoformat()
        }
    else:
        return {"error": "Failed to update card"}


async def add_card(front: str, back: str) -> Dict[str, Any]:
    """Add new flashcard to database.
    
    Args:
        front: Question text
        back: Answer text
        
    Returns:
        Dict with card_id and success message
    """
    repo = Repository()
    repo.init_db()
    card_id = repo.create_card(front, back)
    return {
        "card_id": card_id,
        "message": "Card added successfully"
    }


async def import_cards(csv_filepath: str) -> Dict[str, Any]:
    """Import cards from CSV file.
    
    Args:
        csv_filepath: Path to CSV file with 'front' and 'back' columns
        
    Returns:
        Dict with count of imported cards
    """
    repo = Repository()
    repo.init_db()
    try:
        count = repo.import_from_csv(csv_filepath)
        return {
            "count": count,
            "message": f"Successfully imported {count} cards"
        }
    except Exception as e:
        return {"error": f"Failed to import cards: {str(e)}"}


if __name__ == "__main__":
    import asyncio
    
    # Create and run the MCP server
    server = create_mcp_server()
    asyncio.run(server.run())
