
# * Exercise
'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''


# def sum_pairs(lst, num):
#     pairs = []
#     for x in lst:
#         for y in lst[1:]:
#             new_value = x + y
#             if new_value == num:
#                 pairs.append(x)
#                 pairs.append(y)
#                 return pairs

#     return pairs

def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []


print(sum_pairs([11, 20, 4, 2, 1, 5], 100))
