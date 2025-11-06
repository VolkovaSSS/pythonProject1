from typing import Iterable


def filter_by_currency(transacts: list[dict], currency: str) -> Iterable[dict]:
    """Фильтрует транзакции по валюте"""

    for element in transacts:
        if isinstance(element, dict):
            if element.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency:
                yield element


def transaction_descriptions(transacts: list[dict]) -> Iterable[str]:
    """Возвращает описание транзакции"""

    for element in transacts:
        if isinstance(element, dict):
            yield element.get("description", "")


def card_number_generator(first_num, last_num) -> Iterable[str]:
    """Генерирует номера карт"""

    for num in range(first_num, last_num):
        num_str = str(num).zfill(16)
        yield num_str[0:4] + " " + num_str[4:8] + " " + num_str[8:12] + " " + num_str[12:]






