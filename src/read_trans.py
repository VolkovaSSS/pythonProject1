import csv
import pandas as pd
import logging

logger = logging.getLogger("read_trans")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/read_trans.log", "w", "utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions_csv(data_file: str) -> list:
    """Загружает данные о транзакциях из CSV-файла в словарь:
    id;state;date;amount;currency_name;currency_code;from;to;description"""

    try:
        transactions = []
        logger.info(f'Начало чтения файла {data_file}')
        with open(data_file, encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                transactions.append(row)
        logger.info(f'Конец чтения файла {data_file}')
        return transactions
    except(Exception) as ex:
        logger.error(ex)



def read_transactions_excel(data_file: str) -> list:
    """Загружает данные о транзакциях из Excel-файла в словарь:
    id;state;date;amount;currency_name;currency_code;from;to;description"""

    try:
        logger.info(f'Начало чтения файла {data_file}')
        excel_data = pd.read_excel(data_file)
        transactions = excel_data.to_dict('records')
        logger.info(f'Конец чтения файла {data_file}')
        for i in range(5):
            print(transactions[i])

        return transactions
    except(Exception) as ex:
        logger.error(ex)


if __name__ == '__main__':
    read_transactions_csv("../data/transactions.csv")

if __name__ == '__main__':
    read_transactions_excel("../data/transactions_excel.xlsx")


