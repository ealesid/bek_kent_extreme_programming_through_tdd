
def test_multiplication():

    five_dollars = Dollar(5)
    five_dollars.times(2)

    assert five_dollars.amount == 10
