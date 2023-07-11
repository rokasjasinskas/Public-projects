def main():
    while True:
        divide = input_fraction()
        if divide is None:
            continue
        break

def input_fraction():
    try:
        fraction = input("Fraction: ")
        x, y = map(int, fraction.split('/'))
        divide = x / y
        percent = divide * 100
        while percent <= 100:
            if percent <= 1:
                print ("E")
                return divide
            elif percent >= 99:
                print ("F")
                return divide
            else:
                print(round(percent), "%", sep="")
                return divide
    except (ValueError, ZeroDivisionError):
        return None

main()

# input integer x/y
# split input
# divide input
# round input
# output round inpout with %
# make it loop while true
# put everythin in try: if valueError pass
# if valueError pass
# if other errors pass
#
#
#
#
#
#
#
#
#
