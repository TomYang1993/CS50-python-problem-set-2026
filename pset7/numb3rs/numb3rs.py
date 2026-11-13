import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    match = re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip)
    if not match:
        return False

    for group in match.groups():
        if group != str(int(group)):
            return False
        if not 0 <= int(group) <= 255:
            return False

    return True


if __name__ == "__main__":
    main()
