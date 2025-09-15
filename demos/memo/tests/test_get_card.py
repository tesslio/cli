# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/db.spec.md
# (spec:81f0fca1) (code:e6b9846a)

import pytest
import os
from memo.db import Repository, Card

@pytest.fixture
def test_db():
    """Create test database and clean up after test"""
    db_path = "test_memo.db"
    
    # Clean up any existing test database
    if os.path.exists(db_path):
        os.remove(db_path)
    
    repo = Repository(db_path)
    repo.init_db()
    
    # Pre-populate with sample cards
    repo.create_card("Cat", "Gato")
    repo.create_card("Dog", "Perro") 
    repo.create_card("House", "Casa")
    
    yield repo
    
    # Clean up after test
    if os.path.exists(db_path):
        os.remove(db_path)

def test_get_card_by_id(test_db):
    """Retrieve single cards by ID"""
    repo = test_db
    
    card = repo.get_card(1)
    assert card is not None
    assert card.id == 1
    assert card.front == "Cat"
    assert card.back == "Gato"

def test_get_nonexistent_card_returns_none(test_db):
    """Retrieving a non-existent card returns None"""
    repo = test_db
    
    card = repo.get_card(999)
    assert card is None
