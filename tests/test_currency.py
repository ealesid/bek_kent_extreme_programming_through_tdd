from src.part1.currency import Currency
from src.part1.currency import Bank
from src.part1.currency import Expression
from src.part1.currency import Summ


def test_multiplication():

    five_dollars = Currency.dollar(5)

    product = five_dollars.times(2)
    assert product.amount == 5 * 2
    assert product == Currency.dollar(5 * 2)

    product = five_dollars.times(3)
    assert product.amount == 5 * 3
    assert product == Currency.dollar(5 * 3)

    five_francs = Currency.franc(5)
    assert Currency.franc(10) == five_francs.times(2)
    assert Currency.franc(15) == five_francs.times(3)


def test_equality():

    assert Currency.dollar(5) == Currency.dollar(5)
    assert Currency.dollar(5) != Currency.dollar(6)

    assert Currency.franc(5) == Currency.franc(5)
    assert Currency.franc(5) != Currency.franc(6)

    assert Currency.dollar(5) != Currency.franc(5)


def test_currency():
    assert Currency.dollar(1).currency == 'USD'
    assert Currency.franc(1).currency == 'CHF'


def test_simple_addition():
    summary = Currency.dollar(5) + Currency.dollar(5)
    assert summary == Currency.dollar(10)

    five_dollars: Currency = Currency.dollar(5)
    summ: Expression = five_dollars + five_dollars

    bank: Bank = Bank()
    reduced: Currency = bank.reduce(summ, 'USD')
    assert reduced == Currency.dollar(10)


def test_plus_returns_summ():

    five: Currency = Currency.dollar(5)
    result: Expression = five + five
    summ: Summ = result
    assert five == summ.augend
    assert five == summ.addend


def test_reduce_summ():
    summ: Expression = Summ(Currency.dollar(3), Currency.dollar(4))
    bank: Bank = Bank()
    result: Currency = bank.reduce(summ, 'USD')
    assert result == Currency.dollar(3 + 4)


def test_reduce_money():
    bank: Bank = Bank()
    result: Currency = bank.reduce(Currency.dollar(1), 'USD')
    assert result == Currency.dollar(1)


def test_reduce_money_different_currency():
    bank: Bank = Bank()
    bank.add_rate('CHF', 'USD', 2)
    result: Currency = bank.reduce(Currency.franc(2), 'USD')
    assert result == Currency.dollar(1)


def test_identity_rate():
    assert Bank().rate('USD', 'USD') == 1


def test_mixed_addition():
    five_dollars: Expression = Currency.dollar(5)
    ten_francs: Expression = Currency.franc(10)

    bank: Bank = Bank()
    bank.add_rate('CHF', 'USD', 2)

    result: Currency = bank.reduce(five_dollars + ten_francs, 'USD')
    assert result == Currency.dollar(10)


def test_summ_plus_currency():
    five_dollars: Expression = Currency.dollar(5)
    ten_francs: Expression = Currency.franc(10)

    bank: Bank = Bank()
    bank.add_rate('CHF', 'USD', 2)

    summ: Expression = Summ(five_dollars, ten_francs) + five_dollars
    result: Currency = bank.reduce(summ, 'USD')
    assert result == Currency.dollar(15)


def test_summ_times():
    five_dollars: Expression = Currency.dollar(5)
    ten_francs: Expression = Currency.franc(10)

    bank: Bank = Bank()
    bank.add_rate('CHF', 'USD', 2)

    summ: Expression = Summ(five_dollars, ten_francs).times(2)
    result: Currency = bank.reduce(summ, 'USD')
    assert result == Currency.dollar(20)
