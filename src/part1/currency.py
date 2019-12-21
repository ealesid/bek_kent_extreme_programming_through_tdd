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

    def __add__(self, other):
        return Currency(self.amount + other.amount, self.currency)

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
        return Currency(amount, 'USD')

    @staticmethod
    def franc(amount):
        return Currency(amount, 'CHF')
