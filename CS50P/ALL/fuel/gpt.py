def main():
    while True:
        divide = input_fraction()
        if divide is None:
            continue
        percentage(divide)
        break

def input_fraction():
    try:
        fraction = input("Fraction: ")
        x, y = map(int, fraction.split('/'))
        divide = x / y
        print(divide)
        return divide
    except (ValueError, ZeroDivisionError):
        print("Error: Invalid input.")
        return None

def percentage(divide):
    percent = divide * 100
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(round(percent))

main()