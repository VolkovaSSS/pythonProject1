from unittest.mock import mock_open, patch
import pytest
import pandas as pd
from src.read_trans import read_transactions_csv, read_transactions_excel


@patch("csv.DictReader")
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="""id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;
Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;
Discover 0720428384694643;Перевод с карты на карту""",
)
def test_read_transactions_csv(mock_open, mock_dict_reader):
    """Тест успешного чтения CSV файла"""

    mock_dict_reader.return_value = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    expected_result = [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": "3598919",
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": "29740",
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]

    result = read_transactions_csv("../data/transactions.csv")
    assert result == expected_result


def test_read_transactions_csv_file_not_found():
    """Тест ошибки чтения файла csv"""
    with pytest.raises(Exception):
        read_transactions_csv("../data/no_file.csv")


@patch("pandas.read_excel")
def test_read_transactions_excel_to_dict(mock_read_excel):
    """Тест успешного чтения Excel файла"""
    mock_data = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"],
    }
    mock_df = pd.DataFrame.from_dict(mock_data)
    mock_read_excel.return_value = mock_df
    expected_result = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
    ]
    result = read_transactions_excel("../data/transactions_excel.xlsx")
    assert result == expected_result


def test_read_transactions_excel_no_file():
    """Тест ошибки чтения файла Excel"""
    with pytest.raises(Exception):
        read_transactions_excel("../data/no_file.xlsx")
