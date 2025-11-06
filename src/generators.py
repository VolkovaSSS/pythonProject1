from typing import Iterable


def filter_by_currency(transacts: list[dict], currency: str) -> Iterable:
    """Фильтрует транзакции по валюте"""

    for element in transacts:
        if isinstance(element, dict):
            if element.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency:
                yield element


def transaction_descriptions(transacts: list[dict]) -> Iterable:
    """Возвращает описание транзакции"""

    for element in transacts:
        if isinstance(element, dict):
            yield element.get("description", "")


