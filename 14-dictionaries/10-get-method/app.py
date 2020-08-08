
# * get Method
d = dict(a=1, b=2, c=3)

d['a']  # 1
d.get('a')  # 1

d['b']  # 2
d.get('b')  # 2

print(d)  # {'a': 1, 'b': 2, 'c': 3}

# d['no_key']  # KeyError
# d.get('no_key')  # None
