import json
import os


def read_transactions_file(data_file: str) -> list:
    """Считывает данные о транзакциях из файла в список словарей"""

    if os.path.isfile(data_file):
        if os.path.getsize(data_file) == 0:
            print("файл пустой")
            return []
        with open(data_file, "r", encoding="utf-8") as file:
            try:
                data_list = json.load(file)
                if not isinstance(data_list, list):
                    print("В файле некорректные данные")
                    return []
                else:
                    return data_list
            except json.JSONDecodeError:
                print("Ошибка формата файла")
                return []
    else:
        print(f"Файл {data_file} не найден")
        return []
