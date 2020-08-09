
# * Multiply Even Numbers
# def multiply_even_numbers(lst):
#     total = 1
#     for x in lst:
#         if x % 2 == 0:
#             total *= x
#     return total

def multiply_even_numbers(lst):
    """
    >>> multiply_even_numbers([2,4,6,8,11,13])
    384
    """
    total = 1
    for x in lst:
        if x % 2 == 0:
            total *= x
    return total
