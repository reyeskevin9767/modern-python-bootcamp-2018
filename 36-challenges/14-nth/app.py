
# * Exercise
'''
nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''

# def nth(lst, num):
#     return lst[num]


def nth(arr, idx):
    if idx >= 0:
        return arr[idx]
    return arr[idx + len(arr)]


print(nth(['a', 'b', 'c', 'd'], 1))
print(nth(['a', 'b', 'c', 'd'], -2))
print(nth(['a', 'b', 'c', 'd'], -4))
