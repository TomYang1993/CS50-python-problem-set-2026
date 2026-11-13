from plates import is_valid


def test_valid():
    assert is_valid("CS50") is True
    assert is_valid("AAA222") is True


def test_too_short_or_long():
    assert is_valid("H") is False
    assert is_valid("OUTATIME") is False


def test_leading_zero():
    assert is_valid("CS05") is False


def test_digits_in_middle():
    assert is_valid("AAA22A") is False
    assert is_valid("CS50P") is False


def test_punctuation():
    assert is_valid("PI3.14") is False
