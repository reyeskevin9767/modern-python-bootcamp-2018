
# * List Manipulation
'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

# def list_manipulation(lit, com, loc, val = None):
#     if com == "remove" and loc == "end":
#         return lit.pop()
#     elif com == "remove" and loc == "beginning":
#         return lit.pop(0)
#     elif com == "add" and loc == "end":
#         lit.append(val)
#         return lit
#     elif com == "add" and loc == "beginning":
#         lit.insert(0,val)
#         return lit


def list_manipulation(lit, com, loc, val=None):
    """
    >>> list_manipulation([1,2,3], "add", "beginning", 20)
    [20, 1, 2, 3]
    """
    if com == "remove" and loc == "end":
        return lit.pop()
    elif com == "remove" and loc == "beginning":
        return lit.pop(0)
    elif com == "add" and loc == "end":
        lit.append(val)
        return lit
    elif com == "add" and loc == "beginning":
        lit.insert(0, val)
        return lit
