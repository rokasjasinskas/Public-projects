def main():
    convert(input("test "))
    print (convert)
    show()

def convert(time):
    hours, minutes = time.split(":")
    h = int(hours)
    m = int(minutes)

    if h <= 12:
        name = ((h * 60) + m) / 60
        float(name)

    else:
        h = h - 12
        name = ((h * 60) + m) / 60
        float(name)

def show(time):
    if convert >= 7 and convert <= 8:
        print ("breakfast time")
    elif convert >= 12 and convert <= 13:
        print ("lunch time")
    elif convert >= 18 and convert <= 19:
        print ("dinner time")

main()
