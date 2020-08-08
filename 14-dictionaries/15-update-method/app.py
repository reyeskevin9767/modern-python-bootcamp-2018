
# * Update Method
first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
print(second)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# let's overwrite an existng key
second['a'] = 'AMAZING'

print(second)  # {'a': 'AMAZING', 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# if we update again
second.update(first)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# the update overrides our values
print(second)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
