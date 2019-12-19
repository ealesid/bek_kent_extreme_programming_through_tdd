from src.part1.dollar import Dollar


def test_multiplication():

    five_dollars = Dollar(5)

    product = five_dollars.times(2)
    assert product.amount == 5 * 2

    product = five_dollars.times(3)
    assert product.amount == 5 * 3
