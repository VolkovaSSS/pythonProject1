import re
from collections import Counter


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """фильтрует список словарей по state"""
    return [element for element in transactions if element.get("state") == state]


def sort_by_date(transactions: list[dict], desc: bool = True) -> list[dict]:
    """Сортирует список словарей по дате"""
    return sorted(transactions, key=lambda x: x["date"] if "date" in x else "", reverse=desc)


def process_bank_search(transactions: list[dict], search_str: str) -> list:
    """Поиск операций по подстроке в описании
    Параметры: список словарей с транзакциями, подстрока поиска для отбора
    Возвращает список отобранных словарей
    """
    if not isinstance(transactions, list):
        message = "Неверный формат данных о транзакциях!"
        raise TypeError(message)
    if not isinstance(search_str, str):
        message = "Для поиска должна использоваться строка!"
        raise TypeError(message)
    return [
        item
        for item in transactions
        if re.search(search_str.lower(), str(item.get("description")).lower()) is not None
    ]


def process_bank_operations(transactions: list[dict], categories: list) -> dict:
    """
    Параметры: список словарей с транзакциями и список категорий для отбора
    Возвращает: словарь, где ключ - категория,
    значение - кол-во операций по данной категории"""
    if not isinstance(transactions, list):
        message = "Неверный формат данных о транзакциях!"
        raise TypeError(message)
    if not isinstance(categories, list):
        message = "Неверный формат данных о категориях!"
        raise TypeError(message)
    counter_trans = Counter(item.get("description") for item in transactions if item.get("description") in categories)
    return dict(counter_trans)


transactios = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "description": "Перевод"},
    {"id": 615064595, "date": "2018-10-14T08:21:36.419441", "description": "Перевод"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441", "description": "Поступление"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "description": "Перевод"},
    {"id": 534526727, "state": "UNKNOWN", "date": "2018-09-12T21:27:25.241689", "description": "Поступление"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "description": "Перевод"},
    {},
    {"id": 615064592, "state": "CANCELED", "description": "Перевод"},
    {"id": 615064593, "description": "Списание"},
]
print(process_bank_search(transactios, "прих"))
