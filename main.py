
from src.utils import read_file, filter_operations, sort_by_date, show_ops


def main():
    # Чтение данных из файла
    operations = read_file('operations.json')

    # Фильтрация операций по статусу "Выполнено"
    executed_operations = filter_operations(operations)

    # Сортировка операций по дате
    sorted_operations = sort_by_date(executed_operations)

    # Вывод отсортированных операций в заданном формате
    show_ops(sorted_operations)


if __name__ == '__main__':
    main()
