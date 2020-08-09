
# * Exercise
'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

# def is_odd_string(string):
#     sum = 0
#     for x in string:
#         sum += ord(x)

#     if sum % 2 == 0:
#         return False
#     else:
#         return True


def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1


print(is_odd_string('amazing'))
