from datetime import date, timedelta
import sys
import inflect

p = inflect.engine()

def main():
    #get input from user
    #convert that input to the data format
    #convert data to minutes
    #covert minutes to text
    #print results

    birthday_input = input("Date of Birthday is in format yyyy-mm-dd: ")
    birthday_input_date = birthday_date (birthday_input)
    minutes = date_minutes(birthday_input_date)
    text = convert_text (minutes)
    print (text)


def birthday_date (birthday):
    try:
        year, month, day = map(int, birthday.split("-"))
        return date(year, month, day)

    except ValueError:
        sys.exit("Invalid date")


def date_minutes(birthday):

    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    today = date.today()
    if birthday > today:
        age = birthday - today
        minutes = age.days * 24 * 60
    else:
        age = today - birthday
        minutes = age.days * 24 * 60

    if is_leap_year(birthday.year):
        minutes += 24 * 60

    return minutes


def convert_text(minutes):
    print(type(minutes))
    minutes = 123456
    words = p.number_to_words(minutes)
    return words.capitalize()



if __name__ == "__main__":
    main()