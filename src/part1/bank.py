from src.part1.currency import Currency


class Expression:
    pass


class Bank:

    def reduce(self, source: Expression, to: str) -> Currency:
        return Currency.dollar(10)
