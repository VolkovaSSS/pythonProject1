from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from src.utils import read_transactions_file


@pytest.fixture
def file_data_path():
    base_dir = Path(__file__).resolve().parents[1]
    return Path(f"{base_dir}/data/operations.json")


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"id": 441945886,"state": "EXECUTED", "operationAmount": '
    '{"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}} }]',
)
def test_read_transactions_file_correct(mock_data, file_data_path):
    assert read_transactions_file(file_data_path) == [
        {"id": 441945886, "state": "EXECUTED", "amount": "31957.58", "currency_name": "руб.", "currency_code": "RUB"}
    ]


@patch("builtins.open", new_callable=mock_open, read_data='{"id": 441945886,"state": "EXECUTED" }')
def test_read_transactions_file_wrong(mock_data, file_data_path):
    assert read_transactions_file(file_data_path) == []


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_read_transactions_file_empty(mock_data, file_data_path):
    assert read_transactions_file(file_data_path) == []


@patch("os.path.exists")
def test_file_path_not_find(mock_isfile):
    mock_isfile.return_value = False
    assert read_transactions_file("file_json") == []
