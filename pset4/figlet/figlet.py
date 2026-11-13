import random
import sys

from pyfiglet import Figlet

figlet = Figlet()


def main():
    font = parse_args(sys.argv, figlet.getFonts())
    figlet.setFont(font=font)
    text = input("Input: ")
    print(figlet.renderText(text))


def parse_args(args, fonts):
    if len(args) == 1:
        return random.choice(fonts)

    if len(args) == 3 and args[1] in ("-f", "--font"):
        if args[2] in fonts:
            return args[2]

    sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
