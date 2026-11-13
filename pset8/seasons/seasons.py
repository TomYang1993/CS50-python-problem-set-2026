import sys
from datetime import date

import inflect


def main():
    try:
        birth = get_birth_date(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    minutes = minutes_old(birth)
    print(to_words(minutes))


def get_birth_date(s):
    year, month, day = s.split("-")
    return date(int(year), int(month), int(day))


def minutes_old(birth):
    delta = date.today() - birth
    return round(delta.days * 24 * 60)


def to_words(n):
    p = inflect.engine()
    return p.number_to_words(n, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()
