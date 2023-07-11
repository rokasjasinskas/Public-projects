# install pyfiglet
# import pyfiglet
# import sys
#
# def. input
#   input_text = input("Input: ")
#
# if sys input = 0
#   Font is definde as random
#   set font according input
#   font converstion
#   print converstion
# elif sys input starts with -d or --font and follow with two command line arguments
#   set font accoring input
#   convert name
#   print name
# else:
#   print(error massage)
#   sys.exit


import pyfiglet
import sys
import random

from pyfiglet import Figlet

figlet = Figlet()


def input_funk():
    try:
        input_text = input("Input: ")
        return input_text
    except EOFError:
        print("No input provided")
        sys.exit(1)


# Get the list of available fonts
available_fonts = figlet.getFonts()


def font_render(font_name):
    input_text = input_funk()
    if input_text == "":
        print("No input provided")
        sys.exit(1)
    figlet.setFont(font=font_name)
    rendered_text = figlet.renderText(input_text)
    print(rendered_text)


def main():
    if len(sys.argv) == 2:
        random_font = random.choice(available_fonts)
        font_render(random_font)
    elif (
        len(sys.argv) == 3
        and sys.argv[1] in ["-f", "--font"]
        and sys.argv[2] in available_fonts
    ):
        font_name = sys.argv[2]
        font_render(font_name)
    else:
        print("Invalid usage")
        sys.exit(1)


main()
