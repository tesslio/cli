# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/db.spec.md
# (spec:81f0fca1) (code:8d44b2f8)

import pytest
import os
import tempfile
from memo.db import Repository


class TestDatabaseInitialization:
    def setup_method(self):
        """Setup test database before each test"""
        self.test_db = "test_memo.db"
        # Ensure no test database exists before starting
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        self.repo = Repository(self.test_db)

    def teardown_method(self):
        """Cleanup test database after each test"""
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_creates_database_file_at_memo_db_in_current_directory(self):
        """Creates database file at 'memo.db' in current directory"""
        # Initialize database
        self.repo.init_db()
        
        # Verify database file was created
        assert os.path.exists(self.test_db)

    def test_creates_cards_table_with_proper_schema_including_srs_fields(self):
        """Creates cards table with proper schema including SRS fields"""
        # Initialize database
        self.repo.init_db()
        
        # Connect to database and check table schema
        import sqlite3
        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()
        
        # Get table info for cards table
        cursor.execute("PRAGMA table_info(cards)")
        columns = cursor.fetchall()
        
        # Extract column names
        column_names = [column[1] for column in columns]
        
        # Verify required columns exist
        expected_columns = [
            'id', 'front', 'back', 'repetition', 'easiness', 
            'interval', 'next_date', 'created_at', 'updated_at'
        ]
        
        for col in expected_columns:
            assert col in column_names, f"Column {col} not found in cards table"
        
        conn.close()

    def test_handles_database_creation_safely_no_errors_if_already_exists(self):
        """Handles database creation safely (no errors if already exists)"""
        # Initialize database first time
        self.repo.init_db()
        assert os.path.exists(self.test_db)
        
        # Initialize database second time - should not raise error
        try:
            self.repo.init_db()
            # If we get here, no exception was raised
            assert True
        except Exception as e:
            pytest.fail(f"Database initialization failed when database already exists: {e}")
        
        # Verify database still exists
        assert os.path.exists(self.test_db)
