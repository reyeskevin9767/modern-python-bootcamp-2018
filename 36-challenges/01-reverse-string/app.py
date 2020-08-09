
# * Exercise
'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

# add whatever parameters you deem necessary - good luck!
# def reverse_string(word):
#     return word[::-1]


def reverse_string(str):
    s = ''
    for i, char in enumerate(str[::-1]):
        s += char
    return s


print(reverse_string('awesome'))
