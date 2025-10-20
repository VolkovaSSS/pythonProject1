def get_mask_card_number(card_number: int) -> str:
    """Маскировка номера банковской карты"""

    if not isinstance(card_number, int):
        raise ValueError("Номер карты не числовой!")
        return None
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        return "Номер карты - должен быть 16 знаков!"
    indexes_for_replace = [6, 7, 8, 9, 10, 11]
    hidden_number = ["*" if index in indexes_for_replace else char for index, char in enumerate(card_number_str)]
    mask_number = "".join(hidden_number)
    return mask_number[0:4] + " " + mask_number[4:8] + " " + mask_number[8:12] + " " + mask_number[12:]


def get_mask_account(account_number: int) -> str:
    """Маскировка номера банковского счета"""

    if not isinstance(account_number, int):
        raise ValueError("Номер счёта - не числовой!")
        return None
    account_number_str = str(account_number)
    if len(account_number_str) != 20:
        return "Номер счёта - должен быть из 20 знаков!"

    return "**" + str(account_number)[-4:]
