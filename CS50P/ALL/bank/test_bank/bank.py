def main():
    input_x = input("Greetings: ")
    value_x = value(input_x)
    print("$", value_x)

def value(x):
    x = x.strip().casefold()
    first_letter = x[:1]
    first_word = x[:5]
    if x == "hello":
        return 0
    elif first_word == "hello":
        return 0
    elif first_letter == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()