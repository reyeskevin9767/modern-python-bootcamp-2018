
# * Can pass funcs as args to other funcs
from random import choice


def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total


def square(x):
    return x * x


def cube(x):
    return x * x * x


print(sum(3, square))
print(sum(3, cube))


def make_laugh_func():
    def get_laugh():
        l = choice(("HAHAHAH", 'lol', 'tehehe'))
        return l

    return get_laugh


laugh = make_laugh_func()
print(laugh())


def make_laugh_func2(person):
    def get_laugh():
        laugh = choice(("HAHAHAH", 'lol', 'tehehe'))
        return f"{laugh} {person}"

    return get_laugh


laugh2 = make_laugh_func2("Bob")
print(laugh2())
