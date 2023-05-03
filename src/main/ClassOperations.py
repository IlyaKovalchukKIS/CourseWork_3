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
        self.currency = currency.get('name')

    def __repr__(self):
        return f"ClassOperations:(\n{self.date} - дата перевода\n" \
               f"{self.description} - описание перевода\n" \
               f"{self.from_} - откуда произведен перевод\n" \
               f"{self.to_} - куда произведен перевод\n" \
               f"{self.amount} - сумма перевода\n" \
               f"{self.currency} - валюта перевода)"

    def date_visual(self):
        """Приводит дату в эстетический вид"""
        years, month, day = self.date[:10].split("-")
        return f'{day}.{month}.{years}'

    def card_privacy(self):
        """Цензурит номер карты"""
        if self.from_ is not None:
            grouping = self.from_.split(' ')
            x = grouping[-1]
            privacy_card = x[:4] + ' ' + x[4:6] + ("*" * 2) + " " + ("*" * 4) + " " + x[-4:]
            return f"{' '.join(grouping[:-1])} {privacy_card}"
        else:
            return "Нет данных"

    def check_privacy(self):
        """Цензурит номер счета"""
        if self.to_ is not None:
            grouping = self.to_.split(' ')
            x = grouping[-1]
            privacy_check = "**" + x[-4:]
            return f"{' '.join(grouping[:-1])} {privacy_check}"
        else:
            return 'Нет данных'
