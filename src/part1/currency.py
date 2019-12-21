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

    def __add__(self, addend):
        return Summ(self, addend)

    def reduce(self, to: str):
        return self

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


class Expression:

    @abstractmethod
    def reduce(self, to: str):
        pass


class Bank:

    @staticmethod
    def reduce(source: Expression, to: str) -> Currency:
        return source.reduce(to)


class Summ(Expression):
    augend: Currency
    addend: Currency

    def __init__(self, augend: Currency, addend: Currency):
        self.augend = augend
        self.addend = addend

    def reduce(self, to: str) -> Currency:
        amount: int = self.augend.amount + self.addend.amount
        return Currency(amount, to)
