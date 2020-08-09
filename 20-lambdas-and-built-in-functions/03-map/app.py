
# * Map
l = [1, 2, 3, 4]

doubles = list(map(lambda x: x * 2, l))

#evens  [2, 4, 6, 8]

# * Map
# l2 = [1, 2, 3, 4]

doubles = list(map(lambda x: x*2, l2))

# evens # [2,4,6,8]

# * Map
names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele', },
    {'first': 'Blue', 'last': 'Steele', }
]

first_names = list(map(lambda x: x['first'], names))

# first_names  # ['Rusty', 'Colt', 'Blue']
