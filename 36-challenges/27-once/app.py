
# * Exercise
'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''

# def once(func):
#     once.accumulator = 0
#     def inner(num, num2):
#         if once.accumulator:
#             return None
#         once.accumulator += 1
#         return num + num2


#     return inner


def once(fn):
    fn.is_called = False

    def inner(*args):
        if not(fn.is_called):
            fn.is_called = True
            return fn(*args)
    return inner


def add(a, b):
    return a+b


oneAddition = once(add)

print(oneAddition(2, 2))  # 4
print(oneAddition(2, 2))  # None
