import os

from src.utils import read_transactions_file
from src.read_trans import read_transactions_csv, read_transactions_excel
from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations
from src.generators import filter_by_currency
from src.widget import get_date, mask_account_card, get_string_for_report



file_json = os.path.join(os.getcwd(), "data", "operations.json")
file_csv = os.path.join(os.getcwd(), "data", "transactions.csv")
file_xlsx = os.path.join(os.getcwd(), "data", "transactions_excel.xlsx")


def get_answer_yes_no(question: str) -> bool:
    """Задаёт вопрос пользователю с ожидаемым ответом Да/Нет
    возвращает True/ False"""
    answer = input(question)
    if answer.strip().lower() in ['да', 'д', 'yes', 'y']:
        return True
    else:
        return False


def main():
    """Основная функция проекта"""

    print('Привет! Добро пожаловать в программу работы \nс банковскими транзакциями.')

    main_menu = {1: ('1. Получить информацию о транзакциях из JSON-файла', 'JSON'),
                 2: ('2. Получить информацию о транзакциях из CSV-файла', 'CSV'),
                 3: ('3. Получить информацию о транзакциях из XLSX-файла', 'XLSX')}
    print('Выберите необходимый пункт меню:')
    for value in main_menu.values():
        print(value[0])

    file_type = int(input())
    if file_type in main_menu.keys():
        print(f'Для обработки выбран {main_menu[file_type][1]}-файл.')
    else:
        print("Ошибка! Несуществующий формат:")
        return

    if file_type == 1:
        trans_data = read_transactions_file(file_json)
    elif file_type == 2:
        trans_data = read_transactions_csv(file_csv)
    else:
        trans_data = read_transactions_excel(file_xlsx)

    states = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        print('Введите статус, по которому необходимо выполнить фильтрацию.')
        print(f'Доступные для фильтровки статусы: {" ".join(states)}')
        status = input().strip().upper()
        if status in states:
            print(f'Операции отфильтрованы по статусу {status}.')
            trans_filtered = filter_by_state(trans_data, status)
            break
        else:
            print(f'Статус операции {status} недоступен.')

    params = {}
    date_sort = get_answer_yes_no('Отсортировать операции по дате? Да/Нет ')
    params['date_sort'] = date_sort
    if date_sort:
        print('Отсортировать по возрастанию или по убыванию?')
        date_order = input("по возрастанию/по убыванию ").strip().lower()
        params['date_descending'] = False if date_order == "по возрастанию" else True
    params['ruble'] = get_answer_yes_no('Выводить только рублевые транзакции? Да/Нет ')
    params['word_sort'] = get_answer_yes_no('Отфильтровать список транзакций по определенному слову в описании? Да/Нет ')
    if params['word_sort']:
        params['word'] = input("Введите слово для фильтра: ")

    if params['date_sort']:
        trans_filtered = sort_by_date(trans_filtered, params['date_descending'])
    if params['ruble']:
        trans_filtered = list(filter_by_currency(trans_filtered, "RUB"))
    if params['word_sort']:
        trans_filtered = process_bank_search(trans_filtered, params['word'])

    print("Распечатываю итоговый список транзакций...")
    if not trans_filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(trans_filtered)}")
        for trans in trans_filtered:
            print(get_string_for_report(trans))
            # number_from = trans.get('from', "")
            # masked_number_from = mask_account_card(number_from) if len(number_from) > 0 else ""
            # number_to = trans.get('to', "")
            # masked_number_to = mask_account_card(number_to) if len(number_to) > 0 else ""
            # print(f"{get_date(trans.get('date',''))} {trans.get('description')}")
            # print(f"{masked_number_from} - > {masked_number_to}")
            # print(f"Сумма: {trans.get('amount', 0)} {trans.get('currency_name',"")}")



if __name__ == '__main__':
    main()