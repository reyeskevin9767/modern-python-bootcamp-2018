
# * Index Method
t = (1, 2, 3, 3, 3)
t.index(1)  # 0
# t.index(5)  # ValueError: tuple.index(x): x not in tuple
t.index(3)  # 2 - only the first matching index is returned

print(t)

