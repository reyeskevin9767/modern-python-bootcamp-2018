
# * Single Letter Count Exercise
'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

# define single_letter_count below:
# def single_letter_count(str, ltr):
#     newStr = str.lower()
#     newltr = ltr.lower()

#     return newStr.count(newltr)


# print(single_letter_count('Hello Word', 'h'))

# * define single_letter_count below:
def single_letter_count(str, ltr):
    """
    >>> single_letter_count("HelLo World", "l")
    3
    """
    newStr = str.lower()
    newltr = ltr.lower()

    return newStr.count(newltr)
