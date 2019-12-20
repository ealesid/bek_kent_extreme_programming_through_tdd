class Currency(object):

    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return all([
            self.__class__ == other.__class__,
            self.amount == other.amount
        ])

    @property
    def amount(self):
        return self._amount


class Dollar(Currency):

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Currency):

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
