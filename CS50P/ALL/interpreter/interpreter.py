expression = input("Expression: ").strip()
x, y, z = expression.split(" ")


xint = int(x)
zint = int(z)

if y == "+":
    print(float(xint + zint))
elif y == "-":
    print(float(xint - zint))
elif y == "*":
    print(float(xint * zint))
elif y == "/":
    print(float(xint / zint))

else:
    print("False")