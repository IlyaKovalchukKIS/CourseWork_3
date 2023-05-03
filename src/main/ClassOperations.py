class ClassOperations:

    def __init__(self, date, description, from_, to_, amount, currency):
        """
        Инициализация полей перевода
        :param date: дата перевода
        :param description: описание перевода
        :param from_: откуда произведен перевод
        :param to_: куда произведен перевод
        :param amount: сумма перевода
        :param currency: валюта перевода
        """
        self.date = date
        self.description = description
        self.from_ = from_
        self.to_ = to_
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"ClassOperations:(\n{self.date} - дата перевода\n" \
               f"{self.description} - описание перевода\n" \
               f"{self.from_} - откуда произведен перевод\n" \
               f"{self.to_} - куда произведен перевод\n" \
               f"{self.amount} - сумма перевода\n" \
               f"{self.currency} - валюта перевода)"