# GENERATED FROM SPEC - DO NOT EDIT
# @generated with Tessl v0.21.0-rc3 from ../specs/db.spec.md
# (spec:81f0fca1) (code:88baef91)

import os
import pytest
from memo.db import Repository, Card

@pytest.fixture(autouse=True)
def clean_db():
    db_path = "test_memo.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    yield
    if os.path.exists(db_path):
        os.remove(db_path)

def test_get_all_cards():
    repo = Repository(db_path="test_memo.db")
    repo.init_db()
    fronts = ["Red", "Blue", "Green", "Yellow"]
    backs = ["Rojo", "Azul", "Verde", "Amarillo"]
    created_ids = []
    for front, back in zip(fronts, backs):
        card_id = repo.create_card(front, back)
        created_ids.append(card_id)

    cards = repo.get_all_cards()
    assert len(cards) == 4
    for i, card in enumerate(cards):
        assert isinstance(card, Card)
        assert card.id == created_ids[i]
        assert card.front == fronts[i]
        assert card.back == backs[i]
        assert card.repetition == 0
        assert card.easiness == 2.5
        assert card.interval == 1
        assert isinstance(card.next_date, str)
        assert isinstance(card.created_at, str)
        assert isinstance(card.updated_at, str)
