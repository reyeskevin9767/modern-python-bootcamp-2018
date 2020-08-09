
# * Partition Exercise
def partition(lst, func):
    newlisT = []
    newlisF = []

    for val in lst:
        if func(val):
            newlisT.append(val)
        else:
            newlisF.append(val)
    return [newlisT, newlisF]
