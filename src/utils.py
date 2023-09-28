
import os
import json


def read_file(filename):
    """
    Функция открывает файл формата json.
    :param filename: название файла.
    :return: данные, содержащиеся в файле.
    """
    # Построить путь к файлу operat.json относительно папки src
    operat_path = os.path.join(os.path.dirname(__file__), '..', filename)

    # Открыть файл operations.json и загрузить его содержимое
    with open(operat_path, 'r', encoding="utf8") as file:
        data = json.load(file)

    return data

