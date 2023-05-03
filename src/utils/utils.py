from datetime import datetime
from src.main.ClassOperations import ClassOperations
import json


def load_operations(operations_open=None):
    """
    :param operations_open: список операций в формате json
    :return: открытый список операций
    """
    try:
        with open(operations_open, 'r', encoding='utf-8') as f:
            file = json.load(f)
            return file
    except (TypeError, FileNotFoundError, OSError, AttributeError):
        return None


def key_sort_date(operations_date=None):
    """
    Ключ для сортировки операций по дате
    """
    try:
        return datetime.strptime(operations_date.get('date', '2019-05-19T12:51:49.023880'), "%Y-%m-%dT%H:%M:%S.%f")
    except (TypeError, FileNotFoundError, OSError, AttributeError):
        return None


def sort_operation_date(operations_dict=None):
    """
    :param operations_dict: cписок всех операций
    :return: отсортированный список по дате
    """
    try:
        sort_by_date = sorted(operations_dict, key=key_sort_date, reverse=True)
        return sort_by_date
    except (TypeError, FileNotFoundError, OSError, AttributeError):
        return None


def sort_operation_state(operations_dict=None):
    """
    :param operations_dict: отсортированный список операций по дате
    :return: 5 последних отсортированных операций по дате и статусу
    """
    try:
        sort_by_executed = sorted(operations_dict, key=lambda x: x.get("state") == "EXECUTED", reverse=True)
        return sort_by_executed[:5]
    except (TypeError, FileNotFoundError, OSError, AttributeError):
        return None


def instance_operations(list_operations=None):
    """

    :param list_operations: список отсортированных операций
    по дате и статусу выполнено
    :return: список экземпляров класса
    """
    try:
        instance_list = []
        for operation in list_operations:
            date = operation.get("date")
            description = operation.get('description')
            from_ = operation.get('from')
            to_ = operation.get('to')
            amount = operation.get('operationAmount').get('amount')
            currency = operation.get('operationAmount').get('currency')
            instance_list.append(ClassOperations(date,
                                                 description,
                                                 from_,
                                                 to_,
                                                 amount,
                                                 currency))

        return instance_list

    except (TypeError, AttributeError):
        return None
