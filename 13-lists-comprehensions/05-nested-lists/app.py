
# * Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# * Accessing Nesed Lists
print(nested_list[0][1])  # 2

print(nested_list[1][-1])  # 6

# * Printing Values In Nested Lists
for l in nested_list:
    for val in l:
        print(val)


# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# * Printing Values In Nested Lists
nested_list_Two = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(val) for val in l] for l in nested_list_Two]

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# * Printing Values In Nested Lists
board = [[num for num in range(1, 4)] for val in range(1, 4)]

print(board)  # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# * Printing Values In Nested Lists
print([['X' if num % 2 != 0 else 'O' for num in range(1, 4)]
       for val in range(1, 4)])

# [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]
