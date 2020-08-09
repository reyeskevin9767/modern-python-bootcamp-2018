
# * Last Element
'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

# def last_element(lst):
#     if len(lst) > 0:
#         return lst[-1]
#     else:
#         None

# print(last_element([2,3,4]))


def last_element(lst):
    """
    >>> last_element([2,3,4])
    4
    """

    if len(lst) > 0:
        return lst[-1]
    else:
        None
    return lst[-1]
