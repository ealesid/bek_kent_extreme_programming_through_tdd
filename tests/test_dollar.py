from src.part1.dollar import Dollar, Franc


def test_multiplication():

    five_dollars = Dollar(5)

    product = five_dollars.times(2)
    assert product.amount == 5 * 2
    assert product == Dollar(5 * 2)

    product = five_dollars.times(3)
    assert product.amount == 5 * 3
    assert product == Dollar(5 * 3)


def test_equality():

    assert Dollar(5) == Dollar(5)
    assert Dollar(5) != Dollar(6)

    assert Franc(5) == Franc(5)
    assert Franc(5) != Franc(6)


def test_franc_multiplication():
    five_francs = Franc(5)

    assert Franc(10) == five_francs.times(2)
    assert Franc(15) == five_francs.times(3)
