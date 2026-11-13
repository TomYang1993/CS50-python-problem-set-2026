import os
import sys

from PIL import Image, ImageOps

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png")


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path, output_path = sys.argv[1], sys.argv[2]
    input_ext = os.path.splitext(input_path)[1].lower()
    output_ext = os.path.splitext(output_path)[1].lower()

    if output_ext not in VALID_EXTENSIONS:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    if not os.path.exists(input_path):
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    with Image.open(input_path) as photo:
        photo = ImageOps.fit(photo, shirt.size)
        photo.paste(shirt, shirt)
        photo.save(output_path)


if __name__ == "__main__":
    main()
