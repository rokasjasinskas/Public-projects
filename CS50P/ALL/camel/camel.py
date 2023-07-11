camel_case = input("Enter a variable name in camel case: ")

snake_case = ""

for _ in camel_case:
    if _.isupper():
        snake_case += "_" + _.lower()
    else:
        snake_case += _

print("The variable name in snake case is:", snake_case)
