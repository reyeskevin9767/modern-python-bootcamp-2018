
# * Slice
# * First Parameter for Slice: start
first_list = [1, 2, 3, 4]

print(first_list[1:])  # [2, 3, 4]

print(first_list[3:])  # [4]

# * Second Parameter for Slice: end
second_list = [1, 2, 3, 4]

print(second_list[:2])  # [1, 2]

print(second_list[:4])  # [1, 2, 3, 4]

print(second_list[1:3])  # [2, 3]

# * Third Parameter for Slice: step
third_list = [1, 2, 3, 4, 5, 6]

print(third_list[1::2])  # [2, 4, 6]

print(third_list[::2])  # [1, 3, 5]

print(third_list[1::-1])  # [2, 1]

print(third_list[:1:-1])  # [6, 5, 4, 3]

print(third_list[2::-1])  # [3, 2, 1]
