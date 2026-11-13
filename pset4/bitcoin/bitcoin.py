import sys

import requests

API_KEY = "YourApiKey"


def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={API_KEY}")
        response.raise_for_status()
        price = float(response.json()["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Could not fetch Bitcoin price")

    print(f"${price * n:,.4f}")


if __name__ == "__main__":
    main()
