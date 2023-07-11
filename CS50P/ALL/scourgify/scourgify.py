# implement check variabel def which would if it is:
    # not less than 1
    # not more than 1
    # file exists
    # file is csv
# to change csv info to ASCII art


import sys
import os
from tabulate import tabulate
import csv

def check_variable(input):

    def exit(input):
        print(f"Could not read {input}")
        sys.exit(1)

    try:
        if len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)

        extension = os.path.splitext(input)[1]
        file_path = os.path.join("/workspaces/125792805/scourgify/", input)

        if extension != ".csv":
            exit(input)
        elif not os.path.exists(file_path):
            exit(input)
        else:
            return input

    except IndexError:
        print("Too few command-line arguments")
        sys.exit(1)

def clean (input, output):

    with open(input, newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    fieldnames = ['first', 'last', 'house']

    with open(output, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            name = row['name']
            first, last = name.split(', ')
            writer.writerow({'first': first, 'last': last, 'house': row['house']})

def main ():
    input = sys.argv[1]
    output = sys.argv[2]
    check_variable(input)
    clean (input, output)


if __name__ == "__main__":
    main()
