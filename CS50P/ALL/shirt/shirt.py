import sys
import os
from PIL import Image, ImageOps


def check_variable(input, output):
    def ex(input):
        print(f"Could not read {input}")
        sys.exit(1)

    try:
        if len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)

        extension = os.path.splitext(input.lower())[1]
        extension_out = os.path.splitext(output.lower())[1]
        file_path = os.path.join("/workspaces/125792805/shirt/", input)
        valid_extensions = [".jpg", ".jpeg", ".png"]
        if extension not in valid_extensions:
            ex(input)
        elif extension != extension_out:
            print("Input and Output has different extensions")
            sys.exit(1)
        elif not os.path.exists(file_path):
            ex(input)
        else:
            return input

    except IndexError:
        print("Too few command-line arguments")
        sys.exit(1)


def shirt(input, before1, output):
    shirt = Image.open(input)
    puppet = Image.open(before1)
    puppet = ImageOps.fit(puppet, shirt.size)
    puppet.paste(shirt, shirt)
    puppet.save(output)


def main():
    # input = sys.argv[1]
    # output = sys.argv[2]
    input = "shirt.png"
    output = "cs.png"
    before1 = "before1.jpg"
    check_variable(input, output)
    shirt(input, before1, output)


if __name__ == "__main__":
    main()
