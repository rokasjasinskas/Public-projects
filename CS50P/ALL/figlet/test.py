import pyfiglet
import sys
import random
import signal

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
    figlet.setFont(font=font_name)
    rendered_text = figlet.renderText(input_text)
    print(rendered_text)

def main():
    if len(sys.argv) == 1:
        random_font = random.choice(available_fonts)
        font_render(random_font)
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in available_fonts:
        font_name = sys.argv[2]
        font_render(font_name)
    else:
        print("Invalid usage")
        sys.exit(1)

if __name__ == '__main__':
    main()
import pyfiglet
import sys
import random
import signal

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
    figlet.setFont(font=font_name)
    rendered_text = figlet.renderText(input_text)
    print(rendered_text)

def main():
    if len(sys.argv) == 1:
        random_font = random.choice(available_fonts)
        font_render(random_font)
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in available_fonts:
        font_name = sys.argv[2]
        font_render(font_name)
    else:
        print("Invalid usage")
        sys.exit(1)

if __name__ == '__main__':
    main()
