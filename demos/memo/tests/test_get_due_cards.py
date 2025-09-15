# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/db.spec.md
# (spec:81f0fca1) (code:b2f52ce0)

import sqlite3
from datetime import date, timedelta
from memo.db import Repository

def insert_cards(repo):
    today = date.today()
    past = (today - timedelta(days=5)).isoformat()
    today_str = today.isoformat()
    future1 = (today + timedelta(days=5)).isoformat()
    future2 = (today + timedelta(days=10)).isoformat()
    with sqlite3.connect(repo.db_path) as conn:
        for nd in [past, today_str, future1, future2]:
            conn.execute(
                "INSERT INTO cards (front, back, repetition, easiness, interval, next_date, created_at, updated_at) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                ("front", "back", 0, 2.5, 1, nd, today_str, today_str)
            )
        conn.commit()
    return past, today_str

def test_get_due_cards_returns_due_and_orders(tmp_path):
    db_path = tmp_path / "test_memo.db"
    repo = Repository(db_path=str(db_path))
    repo.init_db()
    past, today = insert_cards(repo)
    cards = repo.get_due_cards()
    assert len(cards) == 2
    assert [c.id for c in cards] == [1, 2]
    assert [c.next_date for c in cards] == [past, today]

def test_get_due_cards_with_limit(tmp_path):
    db_path = tmp_path / "test_memo.db"
    repo = Repository(db_path=str(db_path))
    repo.init_db()
    past, today = insert_cards(repo)
    cards = repo.get_due_cards(limit=1)
    assert len(cards) == 1
    assert cards[0].id == 1
    assert cards[0].next_date == past

def test_get_due_cards_no_limit_returns_same_as_default(tmp_path):
    db_path = tmp_path / "test_memo.db"
    repo = Repository(db_path=str(db_path))
    repo.init_db()
    insert_cards(repo)
    cards_default = repo.get_due_cards()
    cards_none = repo.get_due_cards(limit=None)
    assert len(cards_none) == len(cards_default)
    assert [c.id for c in cards_none] == [c.id for c in cards_default]
    assert [c.next_date for c in cards_none] == [c.next_date for c in cards_default]
