
# * Number Compare Exercise 
'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

# def number_compare(num1, num2):
#     if num1 == num2:
#         return 'Numbers are equal'
#     elif num1 > num2:
#         return 'First is greater'
#     else:
#         return 'Second is greater'


def number_compare(num1, num2):
    """
    >>> number_compare(2,4)
    'Second is greater'

    >>> number_compare(4,4)
    'Numbers are equal'
    """

    if num1 == num2:
        return 'Numbers are equal'
    elif num1 > num2:
        return 'First is greater'
    else:
        return 'Second is greater'
