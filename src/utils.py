import json
import os
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('../logs/utils.log', 'w', 'utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions_file(data_file: str) -> list:
    """Считывает данные о транзакциях из файла в список словарей"""

    if os.path.isfile(data_file):
        logger.info(f'чтение файла: {data_file}')
        if os.path.getsize(data_file) == 0:
            message = f"файл {data_file} пустой"
            logger.warning(message)
            print(message)
            return []
        with open(data_file, "r", encoding="utf-8") as file:
            try:
                data_list = json.load(file)
                if not isinstance(data_list, list):
                    message = "В файле некорректные данные"
                    logger.error(message)
                    print(message)
                    return []
                else:
                    logger.info(f'Получены данные о транзакциях из файла: {data_file}')
                    return data_list
            except json.JSONDecodeError:
                message = f"Ошибка формата файла: {data_file}"
                logger.error(message)
                print(message)
                return []
    else:
        message = f"Файл {data_file} не найден"
        logger.error(message)
        print(message)
        return []

if __name__ == '__main__':
    read_transactions_file('../data/operation.json')
