# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/db.spec.md
# (spec:81f0fca1) (code:ecfde015)

import os
import sqlite3
from datetime import datetime
import pytest
from memo.db import Repository, Card


@pytest.fixture
def temp_db():
    """Create a temporary test database"""
    db_path = "test_memo.db"
    # Clean up any existing test database
    if os.path.exists(db_path):
        os.remove(db_path)
    
    repo = Repository(db_path)
    repo.init_db()
    
    # Pre-populate with 2 cards with specific SRS values
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Card 1: id=1, repetition=1, easiness=2.5, interval=1, next_date="2024-01-15"
    cursor.execute("""
        INSERT INTO cards (id, front, back, repetition, easiness, interval, next_date, created_at, updated_at)
        VALUES (1, 'Test Front 1', 'Test Back 1', 1, 2.5, 1, '2024-01-15', '2024-01-10 10:00:00', '2024-01-10 10:00:00')
    """)
    
    # Card 2: id=2, repetition=3, easiness=2.8, interval=7, next_date="2024-01-20"
    cursor.execute("""
        INSERT INTO cards (id, front, back, repetition, easiness, interval, next_date, created_at, updated_at)
        VALUES (2, 'Test Front 2', 'Test Back 2', 3, 2.8, 7, '2024-01-20', '2024-01-10 10:00:00', '2024-01-10 10:00:00')
    """)
    
    conn.commit()
    conn.close()
    
    yield repo
    
    # Clean up
    if os.path.exists(db_path):
        os.remove(db_path)


def test_update_card_success(temp_db):
    """Test successful card update with new SRS values"""
    repo = temp_db
    
    # Update card 1 with new values
    result = repo.update_card(
        card_id=1,
        repetition=2,
        easiness=2.6,
        interval=3,
        next_date="2024-01-18"
    )
    
    assert result is True
    
    # Verify the card was updated
    updated_card = repo.get_card(1)
    assert updated_card is not None
    assert updated_card.repetition == 2
    assert updated_card.easiness == 2.6
    assert updated_card.interval == 3
    assert updated_card.next_date == "2024-01-18"


def test_update_nonexistent_card_returns_false(temp_db):
    """Test updating a non-existent card returns False"""
    repo = temp_db
    
    # Try to update card with ID that doesn't exist
    result = repo.update_card(
        card_id=999,
        repetition=1,
        easiness=2.5,
        interval=1,
        next_date="2024-01-15"
    )
    
    assert result is False


def test_update_card_automatically_updates_timestamp(temp_db):
    """Test that updating a card automatically updates the timestamp"""
    repo = temp_db
    
    # Get the original updated_at timestamp
    original_card = repo.get_card(1)
    original_updated_at = original_card.updated_at
    
    # Update the card
    repo.update_card(
        card_id=1,
        repetition=5,
        easiness=3.0,
        interval=10,
        next_date="2024-01-25"
    )
    
    # Verify the timestamp was updated
    updated_card = repo.get_card(1)
    assert updated_card.updated_at != original_updated_at
    # The new timestamp should be more recent
    assert updated_card.updated_at > original_updated_at
