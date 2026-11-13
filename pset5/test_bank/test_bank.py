from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0


def test_h():
    assert value("how you doing?") == 20
    assert value("Hi there") == 20


def test_other():
    assert value("what's happening?") == 100
