# def check_variable

# system variam check if it is:
# is less than one
# is more than one
# if end of variable is .py
# if variable name is nor in folder
#
# if yes exit with sys.exit(1) and message
# return true

# def count_variable
# open file which name is variable
# count each line by line
# if line doesnt start with # or space put in library
# count how many line is in library
# return number

# print it

import sys
import os


def main():
        name = check_variable()
        lines_number = count_lines(name)
        print(lines_number)


def check_variable():
    try:
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)

        name = sys.argv[1]
        extension = os.path.splitext(name)[1]
        file_path = os.path.join("/workspaces/125792805/lines/", name)

        if extension != ".py":
            print("Not a Python file")
            sys.exit(1)
        elif not os.path.exists(file_path):
            print("File does not exist")
            sys.exit(1)
        else:
            return name
    except IndexError:
        print("Too few command-line arguments")
        sys.exit(1)


def count_lines(name):
    with open(name) as file:
        lines = file.readlines()
        lines = [
            line
            for line in lines
            if not line.strip().startswith("#") and line.strip() != ""
        ]
        return len(lines)


if __name__ == "__main__":
    main()
