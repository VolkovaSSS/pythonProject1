import os

import requests
from dotenv import load_dotenv
from requests import RequestException


def convert_val_sum(trans: dict) -> float:
    """Конвертирует сумму транзакции в рубли"""

    code_rub = "RUB"
    code_val = trans.get("operationAmount", {}).get("currency", {}).get("code", "")
    amount = trans.get("operationAmount", {}).get("amount", 0)

    if code_val == code_rub:
        return round(float(amount), 2)

    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={code_rub}&from={code_val}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return float(response.json().get("result", 0.0))
    else:
        raise RequestException(response.status_code)
