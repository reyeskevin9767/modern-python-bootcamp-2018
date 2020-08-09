
# * ASCII ART EXERCISE
# import pyfiglet
# from termcolor import colored

# user_input = input("What message do you want to print? ")
# color_input = input("What Color? ")

# output = colored(pyfiglet.figlet_format(user_input), color=color_input)
# print(output)

from pyfiglet import figlet_format
from termcolor import colored
# help(pyfiglet.figlet_format) # figlet_format(text, font='standard', **kwargs)


def print_art(msg, color):
    valid_colors = ('red', 'green', 'yellow', 'blue',
                    'magenta', 'cyan', 'white')
    if color not in valid_colors:
        color = 'magenta'
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


msg = input('What would you like to print? ')
color = input('What color? ')

print_art(msg, color)
