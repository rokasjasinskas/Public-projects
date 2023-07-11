def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

def main():
    text = input("Enter some text: ")
    result = remove_vowels(text)
    print(result)

if __name__ == "__main__":
    main()