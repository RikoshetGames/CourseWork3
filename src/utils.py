
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


def extract_value(json_list, key):
    """
    Извлекает значение заданного ключа из списка словарей и возвращает замаскированный номер счета или карты.
    :param json_list: Список словарей.
    :param key: ключ, из которого необходимо извлечь значение.
    :return: замаскированный номер счета или карты. Значение None, если ключа нет в словаре.
    """
    # Список платежных систем, для которых необходимо маскировать номера карт.
    payment_list = ["MasterCard", "Maestro", "Visa Gold", "Visa Platinum", "Visa Classic", "МИР"]

    for item in json_list: # Выполняемые иттерации по каждому словарю из списка.
        if key in item: # Если ключ найден в словаре, значение будет извлечено.
            value = item[key]
            if value.startswith("Счет"): # Если значение начинается со "Счет", извлекается номер счета.
                account_number = value.split()[-1] # Разделяем строку на список подстрок и извлекаем номер счета.
                masked_number = mask_account(account_number) # Маскируем номер счета с помощью функции.
                return f"Счет {masked_number}"
            else:
                card_number = None
                for card_type in payment_list: # Выполняем итерацию по списку платежных систем.
                    value_list = value.split()
                    if card_type in value: # Проверяем наличие платежной системы в словаре.
                        card_number = value.split()[-1] # Извлекаем номер карты.
                        masked_number = mask_card(card_number) # Маскируем номер карты с помощью функции.
                        if len(value.split()) == 3:
                            return f"{' '.join(value_list[0:2])} {masked_number}"
                        elif len(value.split()) == 2:
                            return f"{' '.join(value_list[0:1])} {masked_number}"
                if card_number is None:
                    return None
    return None


def format_date(date_str):
    """
    Функция переписывает дату в более понятный формат "ДД.ММ.ГГГГ".
    :param date_str: строка с датой в формате, представленном в списке.
    :return: строка с датой в формате "ДД.ММ.ГГГГ".
    """
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
    return date_obj.strftime('%d.%m.%Y')


def show_ops(operations):
    """
    Вывод информации о каждой операции в удобном формате на экран.
    :param operations: список операций, каждая операция представлена в виде словаря.
    :return: None.
    """
    # Проходим по каждой операции в списке операций
    for op in operations:
        date = format_date(op["date"]) # Получаем дату операции
        description = op["description"] # Получаем описание операции
        from_value = extract_value([op], "from")
        to_value = extract_value([op], "to")
        amount = op["operationAmount"]["amount"]
        currency = op["operationAmount"]["currency"]["name"]
        if from_value == None:
            print(f"{date} {description}\n{to_value}\n{amount} {currency}\n")
        else:
            print(f"{date} {description}\n{from_value} -> {to_value}\n{amount} {currency}\n")