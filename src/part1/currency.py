class Expression:
    @staticmethod
    def reduce(bank, to: str):
        pass


class CurrencyPair:
    from_: str
    to: str

    def __init__(self, from_: str, to: str):
        self.from_ =from_
        self.to = to

    def __eq__(self, other):
        return all([
            self.from_ == other.from_,
            self.to == other.to
        ])

    def __hash__(self):
        return 0


class Currency(Expression):

    _currency = None

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return all([
            self.currency == other.currency,
            self.amount == other.amount
        ])

    def __add__(self, addend) -> Expression:
        return Summ(self, addend)

    def reduce(self, bank, to: str):
        rate: int = bank.rate(self.currency, to)
        return Currency(self.amount / rate, to)

    def times(self, multiplier) -> Expression:
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


class Bank:
    rates: dict = {}

    def add_rate(self, from_: str, to: str, rate: int) -> None:
        self.rates[CurrencyPair(from_, to)] = rate

    def rate(self, from_: str, to: str) -> int:
        if from_ == to:
            return 1
        return self.rates.get(CurrencyPair(from_, to))

    def reduce(self, source: Expression, to: str) -> Currency:
        return source.reduce(self, to)


class Summ(Expression):
    augend: Expression
    addend: Expression

    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend

    def __add__(self, addend: Expression) -> Expression:
        return Summ(self, addend)

    def reduce(self, bank: Bank, to: str) -> Currency:
        amount: int = self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        return Currency(amount, to)
