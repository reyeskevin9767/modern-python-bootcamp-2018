
# * Exercise
'''
two_oldest_ages( [1, 2, 10, 8] ) # [8, 10]
two_oldest_ages( [6,1,9,10,4] ) # [9,10]
two_oldest_ages( [4,25,3,20,19,5] ) # [20,25]
'''


# def two_oldest_ages(arr):
#     old_num = max(arr)
#     arr.remove(old_num)
#     old_num2 = max(arr)
#     return [old_num2, old_num]


def two_oldest_ages(ages):
    return sorted(ages)[-2:]


print(two_oldest_ages([1, 2, 10, 8]))
