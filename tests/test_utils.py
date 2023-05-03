from datetime import datetime
from src.utils import utils
from src.main.ClassOperations import ClassOperations
import pytest


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


def test_sort_operations_date():
    assert utils.sort_operation_date(OPERATIONS) == OPERATIONS_RESULT
    assert utils.sort_operation_date('qwer') is None
    assert utils.sort_operation_date([]) is None


def test_sort_operation_state():
    assert utils.sort_operation_state() is None
    assert utils.sort_operation_state([]) == []
    assert utils.sort_operation_state(123) is None
    assert utils.sort_operation_state('Thank you World') is None
    assert utils.sort_operation_state(OPERATIONS) == OPERATIONS_RESULT
