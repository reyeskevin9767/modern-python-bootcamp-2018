
# * Exercise
'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''
list4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# def sum_up_diagonals(lst):
#     left_side = 0
#     right_side = len(lst)
#     sum_up = 0
#     for x in lst:
#         if left_side < len(x):
#             sum_up += x[left_side]
#             left_side += 1
#         if right_side > 0:
#             sum_up += x[right_side - 1]
#             right_side -= 1

#     return sum_up


def sum_up_diagonals(arr):
    total = 0

    for i, val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total


print(sum_up_diagonals(list4))
