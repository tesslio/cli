# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/db.spec.md
# (spec:81f0fca1) (code:28e6a400)

import os
import csv
import pytest
from memo.db import Repository

DB_PATH = "test_memo.db"
CSV_PATH = "test_cards.csv"

@pytest.fixture(autouse=True)
def clean_files():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    if os.path.exists(CSV_PATH):
        os.remove(CSV_PATH)
    yield
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    if os.path.exists(CSV_PATH):
        os.remove(CSV_PATH)

def test_import_from_csv_returns_count_and_creates_cards():
    repo = Repository(DB_PATH)
    repo.init_db()
    rows = [
        ["front", "back"],
        ["Apple", "Manzana"],
        ["Book", "Libro"],
        ["Water", "Agua"],
    ]
    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    count = repo.import_from_csv(CSV_PATH)
    assert count == 3
    cards = repo.get_all_cards()
    assert len(cards) == 3
    expected = [("Apple", "Manzana"), ("Book", "Libro"), ("Water", "Agua")]
    for card, (front, back) in zip(sorted(cards, key=lambda c: c.id), expected):
        assert card.front == front
        assert card.back == back
        assert card.repetition == 0
        assert pytest.approx(card.easiness) == 2.5
        assert card.interval == 1
        assert isinstance(card.next_date, str)

def test_import_from_csv_invalid_columns_raises():
    repo = Repository(DB_PATH)
    repo.init_db()
    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["wrong1", "wrong2"])
        writer.writerow(["X", "Y"])
    with pytest.raises(ValueError):
        repo.import_from_csv(CSV_PATH)
