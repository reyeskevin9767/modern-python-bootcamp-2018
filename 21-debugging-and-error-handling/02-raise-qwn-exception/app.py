
# * Raise Own Exception
# * raise ValueError('invalid value')
def colorize(text, color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    if type(color) is not str:
        raise TypeError('Text Must Be A String')
    if type(text) is not str:
        raise TypeError('Text Must Be A String')
    if color not in colors:
        raise ValueError('Color Is Invalid Color')
    print(f"Printed P{text} in {color}")


colorize("34", 'red')
