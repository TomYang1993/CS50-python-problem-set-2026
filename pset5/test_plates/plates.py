def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s.isalnum():
        return False

    if not s[:2].isalpha():
        return False

    digits_started = False
    for char in s:
        if char.isdigit():
            digits_started = True
        elif digits_started:
            return False

    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and i > 0 and not s[i - 1].isdigit():
                return False
            break

    return True


if __name__ == "__main__":
    main()
