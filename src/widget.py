from src import masks


def count_number_len(account_card: str) -> int:
    """Вычисляет количество цифр карты(счета)"""
    last_space_position = account_card.rfind(" ")
    if last_space_position == -1:
        return 0
    else:
        return len(account_card) - last_space_position - 1


def mask_account_card(account_card: str) -> str:
    """Маскирует номер карты или счета"""

    number_len = count_number_len(account_card)
    account_card_number = account_card[-number_len:]
    if number_len == 16:
        return account_card.replace(account_card_number, masks.get_mask_card_number(int(account_card_number)))
    elif number_len == 20:
        return account_card.replace(account_card_number, masks.get_mask_account(int(account_card_number)))
    else:
        return "Неверный номер карты (счета)"


def get_date(date_full: str) -> str:
    """Преобразует дату в формат ДД.ММ.ГГГГ"""
    return date_full[5:7] + "." + date_full[8:10] + "." + date_full[:4]
