
# * Copy Method
d = dict(a=1, b=2, c=3)
c = d.copy()

print(c)  # {'a': 1, 'b': 2, 'c': 3}
print(c is d)  # False

e = dict(a=6, b=7, c=8)
f = e.copy()

print(e)  # {'a': 1, 'b': 2, 'c': 3}
print(e is f)  # False
