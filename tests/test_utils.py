from datetime import datetime

from src.main.ClassOperations import ClassOperations
from src.utils import utils
from tests.test_ClassOperations import OPERATIONS, OPERATIONS_RESULT
import pytest


@pytest.fixture()
def list_data():
    return None, 123, 'Thank you World'


def test_load_operations():
    assert utils.load_operations(list_data) is None


def test_key_sort_date():
    assert utils.key_sort_date(list_data) is None
    assert utils.key_sort_date({'date': '2019-05-19T12:51:49.023880'}) == datetime(2019, 5, 19, 12, 51, 49, 23880)


def test_sort_operations_date():
    assert utils.sort_operation_date(OPERATIONS) == OPERATIONS_RESULT
    assert utils.sort_operation_date(list_data) is None


def test_sort_operation_state():
    assert utils.sort_operation_state(list_data) is None
    assert utils.sort_operation_state(OPERATIONS) == OPERATIONS_RESULT


def test_instance_operations():
    assert utils.instance_operations(list_data) is None
