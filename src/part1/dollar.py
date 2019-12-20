class Currency(object):

    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    @property
    def amount(self):
        return self._amount


class Dollar(Currency):

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(object):

    def __init__(self, amount):
        self.__amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    @property
    def amount(self):
        return self.__amount
