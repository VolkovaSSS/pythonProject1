import pandas as pd
from src import masks


def count_number_len(account_card: str) -> int:
    """Вычисляет количество цифр карты(счета)"""

    if not isinstance(account_card, str):
        raise TypeError("Неверный тип данных карты(счета)")
    last_space_position = account_card.rfind(" ")
    if last_space_position == -1:
        return 0
    else:
        return len(account_card) - last_space_position - 1


def mask_account_card(account_card: str) -> str:
    """Маскирует номер карты или счета"""

    if not isinstance(account_card, str):
        raise TypeError("Неверный тип данных карты(счета)")
    number_len = count_number_len(account_card)
    if number_len == 0:
        raise ValueError("Не найден номер карты(счета)")
    account_card_number = account_card[-number_len:]

    if not account_card_number.isdigit():
        raise ValueError("Не найден номер карты(счета)")
    if account_card.find("Счет") != -1:
        return account_card.replace(account_card_number, masks.get_mask_account(int(account_card_number)))
    elif number_len == 16:
        return account_card.replace(account_card_number, masks.get_mask_card_number(int(account_card_number)))
    else:
        raise ValueError("Неверный номер карты (счета)")


def get_date(date_full: str) -> str:
    """Преобразует дату 2024-03-11T02:26:18.671407 в формат ДД.ММ.ГГГГ"""

    if not isinstance(date_full, str):
        raise TypeError("Дата должна быть введена, как строка")
    yyyy = date_full[:4]
    mm = date_full[5:7]
    dd = date_full[8:10]
    for date_part in [dd, mm, yyyy]:
        if not date_part.isdigit():
            raise ValueError("Неверный формат даты")
    if len(yyyy) != 4 or len(mm) != 2 or len(dd) != 2:
        raise ValueError("Неверный формат даты")
    return dd + "." + mm + "." + yyyy


def flatten_dict(dic: dict, sep: str = "_") -> dict:
    """Преобразует многоуровневый словарь в одноуровневый"""
    [flat_dict] = pd.json_normalize(dic, sep=sep).to_dict(orient="records")
    return flat_dict


def get_string_for_report(transact: dict) -> str:
    """Формирует строку для итогового отчета.
    Принимает словарь с транзакцией"""

    number_from = transact.get("from", "")
    if number_from == "" or str(number_from) == "nan":
        masked_number_from = ""
    else:
        masked_number_from = mask_account_card(number_from)
    number_to = str(transact.get("to", ""))
    if number_to == "" or str(number_to) == "nan":
        masked_number_to = ""
    else:
        masked_number_to = mask_account_card(number_to)
    amount = transact.get("amount", 0.0)
    currency = transact.get("currency_name", "")

    return (
        f"{get_date(transact.get('date', ''))} {transact.get('description')}\n"
        f"{masked_number_from} - > {masked_number_to}\n"
        f"Сумма: {amount} {currency}\n"
    )
