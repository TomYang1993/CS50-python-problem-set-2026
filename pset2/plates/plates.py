def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: plate must be 2-6 characters long
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: no spaces, punctuation, or symbols — letters and digits only
    if not s.isalnum():
        return False

    # Rule 3: must start with at least two letters
    if not s[:2].isalpha():
        return False

    # Rule 4: once a digit appears, every character after it must also be
    # a digit (numbers can only trail at the end, never sit before a letter)
    digits_started = False
    for char in s:
        if char.isdigit():
            digits_started = True
        elif digits_started:
            return False

    # Rule 5: the first digit of that trailing digit run can't be "0"
    # (Rule 3 already guarantees the first digit can't be at index 0, so
    # s[i - 1] here is always the letter right before it)
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0" and i > 0 and not s[i - 1].isdigit():
                return False
            break

    return True


main()
