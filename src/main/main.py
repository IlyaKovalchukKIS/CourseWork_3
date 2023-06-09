from src.utils import utils
from os import path

OPERATIONS = path.join('../utils/operations.json')


def main(operations):
    load_operations = utils.load_operations(operations)
    if load_operations is None:
        print('Операция недоступна')
        return

    sort_date = utils.sort_operation_date(load_operations)
    sort_state = utils.sort_operation_state(sort_date)
    instance_operations = utils.instance_operations(sort_state)

    for instance in instance_operations:
        print()
        print(f"{instance.date_visual()} {instance.description}\n"
              f"{instance.card_privacy()} -> {instance.check_privacy()}\n"
              f"{instance.amount} {instance.currency}")


if __name__ == '__main__':
    main(OPERATIONS)