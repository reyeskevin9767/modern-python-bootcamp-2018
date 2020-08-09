
# * Pyhton Errors
def first:  # SyntaxError


None = 1  # SyntaxError

return  # SyntaxError

test
# NameError: name 'test' is not defined

len(5)
# TypeError: object of type 'int' has no len()

"awesome" + []
# TypeError: cannot concatenate 'str' and 'list' objects

list = ["hello"]
list[2]
# IndexError: list index out of range

int("foo")
# ValueError: invalid literal for int() with base 10: 'foo'

d = {}
d["foo"]
# KeyError: 'foo'

"awesome".foo
# AttributeError: 'str' object has no attribute 'foo'
