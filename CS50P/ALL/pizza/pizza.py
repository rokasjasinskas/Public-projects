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

def check_variable():
    try:
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)

        name = sys.argv[1]
        extension = os.path.splitext(name)[1]
        file_path = os.path.join("/workspaces/125792805/pizza/", name)

        if extension != ".csv":
            print("Not a CSV file")
            sys.exit(1)
        elif not os.path.exists(file_path):
            print("File does not exist")
            sys.exit(1)
        else:
            return file_path
    except IndexError:
        print("Too few command-line arguments")
        sys.exit(1)

def make_table (file_path):

    with open (file_path, newline="") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
        table_data = [list(row.values()) for row in reader]
        table_data.insert(0, headers)
    return table_data

def convert (table):
    headers = table[0]
    data = table[1:]
    table = tabulate(data, headers, tablefmt="grid")
    return table

def main ():

    name = check_variable()
    table = make_table(name)
    converted = convert(table)
    print(converted)


if __name__ == "__main__":
    main()
