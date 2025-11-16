import requests
import os
from pathlib import Path
from dotenv import load_dotenv


def convert_val_sum(trans: dict) -> float:
    """Конвертирует сумму транзакции в рубли"""

    code_rub = "RUB"
    code_val = trans.get('operationAmount',{}).get('currency',{}).get('code',"")
    amount = trans.get('operationAmount',{}).get('amount',0)

    if code_val == code_rub:
        return amount
    base_dir = Path(__file__).resolve().parents[1]
    path_env = Path(f"{base_dir}/.env")
    if not path_env.is_file():
        raise FileNotFoundError("Не найден файл окружения .env")
    load_dotenv(path_env)
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={code_rub}&from={code_val}&amount={amount}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        aa = response.json()
        return aa['result']
    else:
        print(response.status_code)
        return 0.0


transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
print(convert_val_sum(transaction))




