
# * Exercise
'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''

# def list_check(lst):
#     for x in lst:
#         if not isinstance(x, list):
#             return False
#     return True


def list_check(vals):
    return all(type(l) == list for l in vals)


print(list_check([[], [1], [2, 3]]))
print(list_check([1, True, [], [1], [2, 3]]))
