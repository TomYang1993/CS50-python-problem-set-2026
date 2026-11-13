from um import count


def test_single():
    assert count("hello, um, world") == 1
    assert count("um") == 1


def test_not_substring():
    assert count("yummy") == 0


def test_multiple():
    assert count("Um, thanks, um...") == 2


def test_case_insensitive():
    assert count("Um, thanks for the album.") == 1
