import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", "w", "utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """Маскировка номера банковской карты"""

    if not isinstance(card_number, int):
        message = "Номер карты должен быть целым числом!"
        logger.error(message)
        raise TypeError(message)
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        message = "Номер карты должен быть 16 цифр!"
        logger.error(message)
        raise ValueError(message)
    indexes_for_replace = [6, 7, 8, 9, 10, 11]
    hidden_number = ["*" if index in indexes_for_replace else char for index, char in enumerate(card_number_str)]
    mask_number = "".join(hidden_number)
    logger.info("Маскируем номер карты")
    return mask_number[0:4] + " " + mask_number[4:8] + " " + mask_number[8:12] + " " + mask_number[12:]


def get_mask_account(account_number: int) -> str:
    """Маскировка номера банковского счета"""

    if not isinstance(account_number, int):
        message = "Номер счёта должен быть целым числом!"
        logger.error(message)
        raise TypeError(message)
    account_number_str = str(account_number)
    if len(account_number_str) < 10:
        message = "Неверная длина счёта"
        logger.error(message)
        raise ValueError(message)
    logger.info("Маскируем номер счёта")
    return "**" + str(account_number)[-4:]
