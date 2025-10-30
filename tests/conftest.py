import pytest


@pytest.fixture
def card_number_correct():
    return 7000792289606361


@pytest.fixture
def card_number_str(card_number_correct):
    return "VISA 7000792289606361"