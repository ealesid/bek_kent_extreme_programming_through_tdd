from src.part1.currency import Currency


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
    summary = Currency.dollar(5).plus(Currency.dollar(5))
    assert summary == Currency.dollar(10)
