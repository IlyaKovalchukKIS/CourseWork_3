from datetime import datetime
import json


def load_operations(operations_open=None):
    try:
        with open(operations_open, 'r', encoding='utf-8') as f:
            file = json.load(f)
            return file
    except (TypeError, FileNotFoundError, OSError):
        return None


def key_sort_date(operations_date):
    try:
        return datetime.strptime(operations_date.get('date', '2019-05-19T12:51:49.023880'), "%Y-%m-%dT%H:%M:%S.%f")
    except (TypeError, FileNotFoundError, OSError):
        return None


def sort_operation_date(operations_dict):
    try:
        sort_by_date = sorted(operations_dict, key=key_sort_date, reverse=True)
        return sort_by_date
    except (TypeError, FileNotFoundError, OSError):
        return None


def sort_operation_state(operations_dict):
    try:
        sort_by_executed = sorted(operations_dict, key=lambda x: x.get("state") == "EXECUTED", reverse=True)
        return sort_by_executed
    except (TypeError, FileNotFoundError, OSError):
        return None

# loading = load_operations(OPERATIONS)
# print(loading)
# sor_ = sort_operation_date(loading)
# print(sor_)
# print(sort_operation_state(sor_))
