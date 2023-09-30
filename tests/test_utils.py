from src.utils import *

def test_read_file():
    pass


def test_filter_operations():
    operations = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELLED"},
        {"id": 3, "state": "EXECUTED"},
        {"id": 4},
        {"id": 5, "state": "CANCELLED"},
        {"id": 6, "state": "EXECUTED"},
    ]
    executed_operations = filter_operations(operations)
    assert len(executed_operations) == 3
    assert executed_operations[0]["id"] == 1
    assert executed_operations[1]["id"] == 3
    assert executed_operations[2]["id"] == 6

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
    assert mask_card("1234567890123456") == "1234 56** **** 3456"
    assert mask_card("1111222233334444") == "1111 22** **** 4444"
    assert mask_card("9876543210987654") == "9876 54** **** 7654"


def test_mask_account():
    assert mask_account("12345678901234567890") == "**7890"
    assert mask_account("11112222333344445555") == "**5555"
    assert mask_account("98765432109876543210") == "**3210"


def test_extract_value():
    json_list = [
        {"id": 1, "from": "MasterCard 1234567890123456"},
        {"id": 2, "to": "Visa Classic 1111222233334444"},
        {"id": 3}
    ]
    assert extract_value(json_list, "from") == "MasterCard 1234 56** **** 3456"
    assert extract_value(json_list, "to") == "Visa Classic 1111 22** **** 4444"
    assert extract_value(json_list, None) == None


def test_format_date():
    assert format_date('2022-09-30T12:34:56.789012') == '30.09.2022'
    assert format_date('2023-01-01T00:00:00.000000') == '01.01.2023'
    assert format_date('2021-12-31T23:59:59.999999') == '31.12.2021'


def test_show_ops():
    pass