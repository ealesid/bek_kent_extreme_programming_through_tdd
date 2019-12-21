from abc import ABC
from abc import abstractmethod


class Currency(ABC):

    _currency = None

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return all([
            self.currency == other.currency,
            self.amount == other.amount
        ])

    def times(self, multiplier):
        return Currency(self.amount * multiplier, self.currency)

    @property
    def amount(self):
        return self._amount

    @property
    def currency(self):
        return self._currency

    @staticmethod
    def dollar(amount):
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Franc(amount, 'CHF')


class Dollar(Currency):

    def times(self, multiplier):
        return Currency.dollar(self.amount * multiplier)


class Franc(Currency):

    def times(self, multiplier):
        return Currency.franc(self.amount * multiplier)
