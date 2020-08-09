
# * Max
# max (strings, dicts with same keys)

max([3, 4, 1, 2])  # 4
max((1, 2, 3, 4))  # 4
max('awesome')  # 'w'
max({1: 'a', 3: 'c', 2: 'b'})  # 3

print(max([2, 3, 4, 5, 5, 7]))

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print([min(len(name) for name in names)])
print(min(len(name) for name in names))

print(max(names, key=lambda n: len(n)))

# * Min
# min (strings, dicts with same keys)
min([3, 4, 1, 2])  # 1
min((1, 2, 3, 4))  # 1
min('awesome')  # 'a'
min({1: 'a', 3: 'c', 2: 'b'})  # 1
