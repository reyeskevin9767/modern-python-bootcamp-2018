
# * TermColor
from termcolor import colored

text = colored('Hi, there', color='magenta',
               on_color='on_cyan', attrs=['blink'])
print(text)
