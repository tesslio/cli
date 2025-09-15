# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/db.spec.md
# (spec:eb029493) (code:ec640067)

from datetime import datetime, date
import sqlite3
import csv
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


class Repository:
    def __init__(self, db_path: str = "memo.db"):
        self.db_path = db_path

    def init_db(self) -> None:
        """Initialize database and create tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                front TEXT NOT NULL,
                back TEXT NOT NULL,
                repetition INTEGER NOT NULL,
                easiness REAL NOT NULL,
                interval INTEGER NOT NULL,
                next_date TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def create_card(self, front: str, back: str) -> int:
        """Create new card with default SRS values. Returns card ID."""
        created_at = datetime.now().isoformat()
        next_date = date.today().isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO cards (front, back, repetition, easiness, interval, next_date, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (front, back, 0, 2.5, 1, next_date, created_at, created_at),
        )
        conn.commit()
        card_id = cursor.lastrowid
        conn.close()
        return card_id

    def get_card(self, card_id: int) -> Optional[Card]:
        """Get single card by ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, front, back, repetition, easiness, interval, next_date, created_at, updated_at FROM cards WHERE id = ?",
            (card_id,),
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Card(*row)
        return None

    def update_card(
        self,
        card_id: int,
        repetition: int,
        easiness: float,
        interval: int,
        next_date: str,
    ) -> bool:
        """Update card's SRS values. Returns True if successful."""
        updated_at = datetime.now().isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE cards
            SET repetition = ?, easiness = ?, interval = ?, next_date = ?, updated_at = ?
            WHERE id = ?
        """,
            (repetition, easiness, interval, next_date, updated_at, card_id),
        )
        conn.commit()
        success = cursor.rowcount > 0
        conn.close()
        return success

    def get_due_cards(self, limit: Optional[int] = None) -> List[Card]:
        """Get cards where next_date <= today, ordered by next_date"""
        today = date.today().isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        query = """
            SELECT id, front, back, repetition, easiness, interval, next_date, created_at, updated_at
            FROM cards
            WHERE next_date <= ?
            ORDER BY next_date ASC
        """
        params = [today]
        if limit is not None:
            query += " LIMIT ?"
            params.append(limit)
        cursor.execute(query, tuple(params))
        rows = cursor.fetchall()
        conn.close()
        return [Card(*row) for row in rows]

    def import_from_csv(self, csv_path: str) -> int:
        """Bulk import cards from CSV file. Returns number of cards imported."""
        count = 0
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if "front" not in reader.fieldnames or "back" not in reader.fieldnames:
                raise ValueError("CSV must contain 'front' and 'back' columns")
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            for row in reader:
                front = row.get("front")
                back = row.get("back")
                if front is None or back is None:
                    continue
                created_at = datetime.now().isoformat()
                next_date = date.today().isoformat()
                cursor.execute(
                    """
                    INSERT INTO cards (front, back, repetition, easiness, interval, next_date, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                    (front, back, 0, 2.5, 1, next_date, created_at, created_at),
                )
                count += 1
            conn.commit()
            conn.close()
        return count

    def get_all_cards(self) -> List[Card]:
        """Get all cards from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, front, back, repetition, easiness, interval, next_date, created_at, updated_at
            FROM cards
        """)
        rows = cursor.fetchall()
        conn.close()
        return [Card(*row) for row in rows]
