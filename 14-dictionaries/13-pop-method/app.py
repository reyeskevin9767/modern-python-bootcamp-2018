
# * Pop Methods
d = dict(a=1, b=2, c=3)
# d.pop()  # TypeError: pop expected at least 1 arguments, got 0

d.pop('a')  # 1

print(d)  # {'c': 3, 'b': 2}

# d.pop('e')  # KeyError

