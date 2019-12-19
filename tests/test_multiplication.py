from src.part1.dollar import Dollar


def test_multiplication():

    five_dollars = Dollar(5)

    five_dollars.times(2)
    assert five_dollars.amount == 5 * 2

    five_dollars.times(3)
    assert five_dollars.amount == 5 * 3
