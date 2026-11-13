from twttr import shorten


def test_mixed_case():
    assert shorten("Twitter") == "Twttr"


def test_all_vowels():
    assert shorten("AEIOUaeiou") == ""


def test_no_vowels():
    assert shorten("CS50") == "CS50"


def test_sentence():
    assert shorten("What's your name?") == "Wht's yr nm?"
