MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            month, day, year = int(month), int(day), int(year)
        else:
            month_name, rest = date.split(" ", 1)
            day, year = rest.replace(",", "").split()
            month, day, year = MONTHS.index(month_name) + 1, int(day), int(year)

        if not (1 <= month <= 12) or not (1 <= day <= 31):
            continue

        print(f"{year}-{month:02}-{day:02}")
        break
    except (ValueError, IndexError):
        continue
