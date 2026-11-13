import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file, output_file = sys.argv[1], sys.argv[2]

    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in rows:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})


if __name__ == "__main__":
    main()
