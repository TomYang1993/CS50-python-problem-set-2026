import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)", s
    )
    if not match:
        raise ValueError("invalid format")

    h1, m1, p1, h2, m2, p2 = match.groups()
    start = to_24_hour(h1, m1, p1)
    end = to_24_hour(h2, m2, p2)
    return f"{start} to {end}"


def to_24_hour(hour, minute, period):
    hour, minute = int(hour), int(minute) if minute else 0
    if not (1 <= hour <= 12) or not (0 <= minute <= 59):
        raise ValueError("invalid time")

    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
