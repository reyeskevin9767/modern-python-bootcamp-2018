
# * Exercise
'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

# def same_frequency(num1, num2):
#     string_1 = str(num1)
#     string_2 = str(num2)
#     dict1 = {x: string_1.count(x) for x in string_1}
#     dict2 = {x: string_2.count(x) for x in string_2}
#     if dict1 == dict2:
#         return True
#     return False


def same_frequency(num1, num2):
    d1 = {letter: str(num1).count(letter) for letter in str(num1)}
    d2 = {letter: str(num2).count(letter) for letter in str(num2)}

    for key, val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True


print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
