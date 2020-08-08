
# * PopItem Method
d = dict(a=1, b=2, c=3, d=4, e=5)

d.popitem()  # ('e', 5)

print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# d.popitem('a')  # TypeError: popitem() takes no arguments (1 given)
