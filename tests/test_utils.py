from datetime import datetime

from src.utils import utils
from src.main.ClassOperations import ClassOperations
import pytest

OPERATIONS = [
    {"id": 2, "state": "CANCELLED", "date": "2019-08-26T10:50:58.294041"},
    {"id": 1, "state": "EXECUTED", "date": "2021-10-01T10:50:58.294041"}
]

OPERATIONS_RESULT = [
    {"id": 1, "state": "EXECUTED", "date": "2021-10-01T10:50:58.294041"},
    {"id": 2, "state": "CANCELLED", "date": "2019-08-26T10:50:58.294041"}
]


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


# def test_instance_operations():
def test_instance_operations():
    list_operations = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]
    instance_list = utils.instance_operations(list_operations)
    assert len(instance_list) == 2
    assert isinstance(instance_list[0], ClassOperations)
    assert isinstance(instance_list[1], ClassOperations)
    assert instance_list[0].date == "2019-08-26T10:50:58.294041"
    assert instance_list[0].description == "Перевод организации"
    assert instance_list[0].from_ == "Maestro 1596837868705199"
    assert instance_list[0].to_ == "Счет 64686473678894779589"
    assert instance_list[0].amount == "31957.58"
    assert instance_list[0].currency == "руб."
    assert instance_list[1].date == "2019-07-03T18:35:29.512364"
    assert instance_list[1].description == "Перевод организации"
    assert instance_list[1].from_ == "MasterCard 7158300734726758"
    assert instance_list[1].to_ == "Счет 35383033474447895560"
    assert instance_list[1].amount == "8221.37"
    assert instance_list[1].currency == "USD"
