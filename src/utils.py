import json
import os
from pathlib import Path


def read_transactions_file(data_file: str) -> list:
    """Считывает данные о транзакциях из файла в список словарей"""

    if os.path.isfile(data_file):
        with open(data_file, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    else:
        return []


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    res = read_transactions_file(os.path.join(BASE_DIR, "data", "operations.json"))
    print(res)
