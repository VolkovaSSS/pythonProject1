import csv
import pandas as pd
import logging
from pathlib import Path

logger = logging.getLogger("read_trans")
logger.setLevel(logging.DEBUG)
BASE_DIR = Path(__file__).resolve().parent.parent
file_handler = logging.FileHandler(BASE_DIR / "logs" / "read_trans.log", "w", "utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions_csv(data_file: str) -> list:
    """Загружает данные о транзакциях из CSV-файла в словарь:
    id;state;date;amount;currency_name;currency_code;from;to;description"""

    try:
        transactions = []
        logger.info(f"Начало чтения файла {data_file}")
        with open(data_file, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                transactions.append(row)
        logger.info(f"Конец чтения файла {data_file}")
        return transactions
    except Exception as ex:
        logger.error(ex)
        raise Exception(f"Ошибка при чтении файла: {ex}")


def read_transactions_excel(data_file: str) -> list:
    """Загружает данные о транзакциях из Excel-файла в словарь:
    id;state;date;amount;currency_name;currency_code;from;to;description"""

    try:
        logger.info(f"Начало чтения файла {data_file}")
        excel_data = pd.read_excel(data_file)
        transactions = excel_data.to_dict("records")
        logger.info(f"Конец чтения файла {data_file}")
        return list(transactions)
    except Exception as ex:
        logger.error(ex)
        raise Exception(f"Ошибка при чтении файла: {ex}")
