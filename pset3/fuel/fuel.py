while True:
    fraction = input("Fraction: ")
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if x > y or y == 0:
            continue
        percentage = round(x / y * 100)
        break
    except (ValueError, ZeroDivisionError):
        continue

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
