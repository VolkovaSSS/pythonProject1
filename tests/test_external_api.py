import os
from unittest.mock import patch

import pytest
from dotenv import load_dotenv

from src.external_api import convert_val_sum

load_dotenv()
API_KEY = os.getenv("API_KEY")


@pytest.fixture
def transaction_rub():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "2000.40", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


@patch("requests.get")
def test_convert_val_sum(mock_get):

    test_data_usd = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }

    mock_get.return_value.json.return_value = {"result": 664923.186244}
    mock_get.return_value.status_code = 200
    assert convert_val_sum(test_data_usd) == 664923.186244
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37",
        headers={"apikey": API_KEY},
    )


def test_convert_val_sum_rub(transaction_rub):
    assert convert_val_sum(transaction_rub) == 2000.40
