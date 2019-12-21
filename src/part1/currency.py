from abc import ABC
from abc import abstractmethod


class Currency(ABC):

    _currency = None

    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return all([
            self.__class__ == other.__class__,
            self.amount == other.amount
        ])

    @abstractmethod
    def times(self, multiplier):
        pass

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)


class Dollar(Currency):

    def __init__(self, amount):
        super().__init__(amount)
        self._currency = 'USD'

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Currency):

    def __init__(self, amount):
        super().__init__(amount)
        self._currency = 'CHF'

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
