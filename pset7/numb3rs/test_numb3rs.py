from numb3rs import validate


def test_valid():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("0.0.0.0") is True


def test_out_of_range():
    assert validate("512.512.512.512") is False
    assert validate("1.2.3.1000") is False


def test_leading_zero():
    assert validate("192.168.001.1") is False


def test_non_numeric():
    assert validate("cat") is False
