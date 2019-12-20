from abc import ABC
from abc import abstractmethod


class Currency(ABC):

    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return all([
            self.__class__ == other.__class__,
            self.amount == other.amount
        ])

    @abstractmethod
    def currency(self):
        pass

    @abstractmethod
    def times(self, multiplier):
        pass

    @property
    def amount(self):
        return self._amount

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)


class Dollar(Currency):

    def currency(self):
        return 'USD'

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)


class Franc(Currency):

    def currency(self):
        return 'CHF'

    def times(self, multiplier):
        return Franc(self.amount * multiplier)
