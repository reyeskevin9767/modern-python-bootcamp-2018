
# * Generator Expressions
g = (num for num in range(1, 10))

for x in range(9):
    print(next(g))
