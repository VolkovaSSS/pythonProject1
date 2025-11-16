import pytest
from unittest.mock import patch
from src.external_api import convert_val_sum
from dotenv import load_dotenv


@pytest.fixture
def transaction_test():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
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
    assert convert_val_sum(test_data_usd) == 664923.186244
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37",
        headers={"apikey": "46hlOny7SNZ6UZm0LP5g5UfKZUyXBqQZ"},
    )


url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=10"
res = {
    "date": "2025-11-16",
    "info": {"rate": 80.879159, "timestamp": 1763329027},
    "query": {"amount": 10, "from": "USD", "to": "RUB"},
    "result": 808.79159,
    "success": True,
}
