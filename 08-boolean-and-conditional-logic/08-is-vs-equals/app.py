
# * is Vs. '=='
a = 1
print(a == 1)  # True
print(a is 1)  # True

# * is Vs. '=='
a = [1, 2, 3]  # a list of numbers
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False

c = b
print(b is c)  # True
