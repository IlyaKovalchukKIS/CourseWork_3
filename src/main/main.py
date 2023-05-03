from src.utils import utils
from os import path

OPERATIONS = path.join('../utils/operations.json')


def main():
    load_operations = utils.load_operations(OPERATIONS)
    if load_operations is None:
        print('Операция недоступна')
        return

    sort_date = utils.sort_operation_date(load_operations)
    sort_state = utils.sort_operation_state(sort_date)
    instance_operations = utils.instance_operations(sort_state)


if __name__ == '__main__':
    main()