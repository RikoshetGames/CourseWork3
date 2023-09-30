from src.utils import *

def test_read_file():
    pass


def test_filter_operations():
    operations = [
        {'id': 1, 'state': 'EXECUTED', 'amount': 100},
        {'id': 2, 'state': 'PENDING', 'amount': 200},
        {'id': 3, 'state': 'EXECUTED', 'amount': 150},
        {'id': 4, 'amount': 50},
        {'id': 5, 'state': 'CANCELLED', 'amount': 75},
        {'id': 6, 'state': 'EXECUTED', 'amount': 300},
    ]
    executed_operations = filter_operations(operations)
    assert len(executed_operations) == 3
    assert executed_operations[0]['id'] == 1
    assert executed_operations[1]['id'] == 3
    assert executed_operations[2]['id'] == 6

def test_sort_by_date():
    operations = [
        {"date": "2022-01-01", "amount": 100},
        {"date": "2022-01-03", "amount": 200},
        {"date": "2022-01-02", "amount": 150},
        {"date": "2022-01-05", "amount": 50},
        {"date": "2022-01-04", "amount": 75},
        {"date": "2022-01-06", "amount": 300},
    ]
    sorted_operations = sort_by_date(operations, num=3)
    assert len(sorted_operations) == 3
    assert sorted_operations[0]["date"] == "2022-01-06"
    assert sorted_operations[1]["date"] == "2022-01-05"
    assert sorted_operations[2]["date"] == "2022-01-04"


def test_mask_card():
    pass


def test_mask_account():
    pass


def test_extract_value():
    pass


def test_format_date():
    pass


def test_show_ops():
    pass