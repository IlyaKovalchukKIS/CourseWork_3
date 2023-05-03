from datetime import datetime
from src.utils import utils
import pytest

OPERATIONS = [
    {"id": 2, "state": "CANCELLED", "date": "2021-10-02"},
    {"id": 1, "state": "EXECUTED", "date": "2021-10-01"}
]

OPERATIONS_RESULT = [
    {"id": 1, "state": "EXECUTED", "date": "2021-10-01"},
    {"id": 2, "state": "CANCELLED", "date": "2021-10-02"}
]


def test_load_operations():
    assert utils.load_operations() is None
    assert utils.load_operations([]) is None
    assert utils.load_operations(123) is None
    assert utils.load_operations('Thank you World') is None


def test_key_sort_date():
    assert utils.key_sort_date() is None
    assert utils.key_sort_date([]) is None
    assert utils.key_sort_date(123) is None
    assert utils.key_sort_date('Thank you World') is None
    assert utils.key_sort_date({'date': '2019-05-19T12:51:49.023880'}) == datetime(2019, 5, 19, 12, 51, 49, 23880)


def test_sort_operation_state():
    assert utils.sort_operation_state() is None
    assert utils.sort_operation_state([]) == []
    assert utils.sort_operation_state(123) is None
    assert utils.sort_operation_state('Thank you World') is None
    assert utils.sort_operation_state(OPERATIONS) == OPERATIONS_RESULT


def test_instance_operations():
    assert utils.instance_operations() is None
    assert utils.instance_operations([]) == []
    assert utils.instance_operations(123) is None
    assert utils.instance_operations('Thank you World') is None
