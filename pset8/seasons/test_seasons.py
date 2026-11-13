from datetime import date

from seasons import minutes_old, to_words


def test_minutes_old_one_year():
    today = date.today()
    one_year_ago = today.replace(year=today.year - 1)
    assert minutes_old(one_year_ago) in (525600, 527040)


def test_minutes_old_zero():
    assert minutes_old(date.today()) == 0


def test_to_words_small():
    assert to_words(100) == "One hundred minutes"


def test_to_words_large():
    assert to_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
