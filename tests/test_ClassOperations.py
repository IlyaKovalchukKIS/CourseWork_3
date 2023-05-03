from src.main.ClassOperations import ClassOperations

OPERATIONS = [
    {"id": 2, "state": "CANCELLED", "date": "2019-08-26T10:50:58.294041"},
    {"id": 1, "state": "EXECUTED", "date": "2021-10-01T10:50:58.294041"}
]

OPERATIONS_RESULT = [
    {"id": 1, "state": "EXECUTED", "date": "2021-10-01T10:50:58.294041"},
    {"id": 2, "state": "CANCELLED", "date": "2019-08-26T10:50:58.294041"}
]


def test_class_operations():
    class_operations = ClassOperations(date="2019-08-26T10:50:58.294041",
                                       description="Перевод организации",
                                       from_="Maestro 1596837868705199",
                                       to_="Счет 64686473678894779589",
                                       amount="8221.37",
                                       currency={
                                           "name": "USD",
                                           "code": "USD"
                                       })

    assert class_operations.__repr__() == f"ClassOperations:(\n2019-08-26T10:50:58.294041 - дата перевода\n" \
                                          f"Перевод организации - описание перевода\n" \
                                          f"Maestro 1596837868705199 - откуда произведен перевод\n" \
                                          f"Счет 64686473678894779589 - куда произведен перевод\n" \
                                          f"8221.37 - сумма перевода\n" \
                                          f"USD - валюта перевода)"

    assert class_operations.date == "2019-08-26T10:50:58.294041"
    assert class_operations.description == "Перевод организации"
    assert class_operations.from_ == "Maestro 1596837868705199"
    assert class_operations.to_ == "Счет 64686473678894779589"
    assert class_operations.amount == "8221.37"
    assert class_operations.currency == "USD"
    assert class_operations.date_visual() == '26.08.2019'
    assert class_operations.card_privacy() == "Maestro 1596 83** **** 5199"
    assert class_operations.check_privacy() == "Счет **9589"
    class_operations_none = ClassOperations([], [], [], [], [], [])
    assert class_operations_none.card_privacy() == "Нет данных"
    assert class_operations_none.check_privacy() == "Нет данных"
    assert class_operations_none.currency == 'Нет данных'
