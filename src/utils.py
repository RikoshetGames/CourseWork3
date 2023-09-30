
import os
import json
from datetime import datetime

def read_file(filename):
    """
    Функция открывает файл формата json.
    :param filename: название файла.
    :return: данные, содержащиеся в файле.
    """
    # Построить путь к файлу operations.json относительно папки src
    operat_path = os.path.join(os.path.dirname(__file__), '..', filename)

    # Открыть файл operations.json и загрузить его содержимое
    with open(operat_path, 'r', encoding="utf8") as file:
        data = json.load(file)
    return data


def filter_operations(operations):
    """
    Функция фильтрует операции по статусу "Выполнено".
    :param operations: список всех доступных операций.
    :return: список операций по статусу "Executed".
    """
    executed_operations = []
    for ops in operations:
        if "state" in ops and ops["state"] == "EXECUTED":
            executed_operations.append(ops)
    return executed_operations


def sort_by_date(operations, num=5):
    """
    Функция сортирует список словарей по дате.
    :param operations: Список операций.
    :param num: параметр, указывающий на количество.
    :return: Отсортированный список.
    """
    sorted_operations = []
    for ops in sorted(operations, key=lambda ops: ops['date'], reverse=True):
        sorted_operations.append(ops)
        if len(sorted_operations) == num:
            break
    return sorted_operations


def mask_card(card_number):
    """
    принимает на вход номер кредитной карты и возвращает его маскированную версию.
    Первые 6 и последние 4 цифры остаются видимыми, остальные маскируются символами *.
    :param card_number: номер карты.
    :return: замаскированный номер.
    """
    masked_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
    return masked_number



def mask_account(account_number):
    """
    принимает на вход номер банковского счета и возвращает его маскированную версию.
    :param account_number: номер банковского счета.
    :return: маскированная версия номера.
    """
    masked_number = '**' + account_number[-4:]
    return masked_number


