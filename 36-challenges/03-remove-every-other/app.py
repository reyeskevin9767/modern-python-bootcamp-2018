
# * Exercise
'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''


# def remove_every_other(lst):
#     new_list = []
#     for (index, x) in enumerate(lst):
#         if (index % 2) == 0:
#             new_list.append(lst[index])
#     return new_list

def remove_every_other(lst):
    return [val for i, val in enumerate(lst) if i % 2 == 0]


print(remove_every_other([1, 2, 3, 4, 5]))
print(remove_every_other([5, 1, 2, 4, 1]))
print(remove_every_other([1]))

# 1 0 -
# 2 1
# 3 2 -
# 4 3
# 5 4 -
