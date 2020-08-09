
# * Built-in Modules Exercise 2
import keyword


def contains_keyword(*args):
    return any([keyword.iskeyword(arg) for arg in args])
