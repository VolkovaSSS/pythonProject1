from typing import Iterator


def filter_by_currency(transacts: list[dict], currency: str) -> Iterator:
    """Фильтрует транзакции по валюте"""

    if not isinstance(transacts, list):
        raise TypeError()
    return (
        trans
        for trans in transacts
        if (
            isinstance(trans, dict)
            and trans.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency
        )
    )


def transaction_descriptions(transacts: list[dict]) -> Iterator:
    """Возвращает описание транзакции"""
    if not isinstance(transacts, list):
        raise TypeError("Некорректные данные")
    for transaction in transacts:
        if isinstance(transaction, dict):
            yield transaction.get("description", "")


def card_number_generator(first_num, last_num) -> Iterator:
    """Генерирует номера карт"""

    if not all([isinstance(first_num, int), isinstance(last_num, int)]):
        raise TypeError("Номер счёта должен быть целым числом!")
    if first_num > last_num:
        raise ValueError("Конечный номер не может быть больше начального")
    if first_num > 9999999999999999 or last_num > 9999999999999999 or first_num <= 0 or last_num <= 0:
        raise ValueError("Номер должен быть в диапазоне от 0 до 9999999999999999")
    for num in range(first_num, last_num + 1):
        num_str = str(num).zfill(16)
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
