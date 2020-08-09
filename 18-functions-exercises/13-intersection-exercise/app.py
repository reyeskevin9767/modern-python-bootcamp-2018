
# * Intersection Exercise
# def intersection(lst1,lst2):
#     both_lst = []
#     for x in lst1:
#         if lst2.count(x) >=1:
#             both_lst.append(x)
#     return both_lst

def intersection(lst1, lst2):
    """
    >>> intersection([1,2,3],[2,3,5,6,7])
    [2, 3]
    """
    both_lst = []
    for x in lst1:
        if lst2.count(x) >= 1:
            both_lst.append(x)
    return both_lst
