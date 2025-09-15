# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/db.spec.md
# (spec:81f0fca1) (code:0582f50f)

import pytest
import os
from datetime import datetime
from memo.db import Repository, Card


class TestCreateCard:
    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        """Setup test database before each test and clean up after"""
        self.test_db_path = "test_memo.db"
        # Remove test database if it exists
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)
        
        # Create repository and initialize database
        self.repo = Repository(self.test_db_path)
        self.repo.init_db()
        
        yield
        
        # Clean up test database
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)

    def test_create_new_card_with_default_srs_values(self):
        """Create new cards with front/back text and default SRS values"""
        # Test data
        front = "Hello"
        back = "Hola"
        
        # Create card
        card_id = self.repo.create_card(front, back)
        
        # Verify card was created and ID was returned
        assert isinstance(card_id, int)
        assert card_id > 0
        
        # Retrieve card to verify it was created with correct values
        created_card = self.repo.get_card(card_id)
        
        assert created_card is not None
        assert created_card.id == card_id
        assert created_card.front == front
        assert created_card.back == back
        assert created_card.repetition == 0
        assert created_card.easiness == 2.5
        assert created_card.interval == 1
        assert created_card.next_date is not None
        assert created_card.created_at is not None
        assert created_card.updated_at is not None
