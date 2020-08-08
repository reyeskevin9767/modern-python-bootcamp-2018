
# * Del
first_list = [1, 2, 3, 4]

del first_list[3]

print(first_list)  # [1, 2, 3]

del first_list[1]

print(first_list)  # [1, 3]

# * Del
second_list = [11, 32, 34, 43, 64, 34]

del second_list[1]

print(second_list)  # [11, 34, 43, 64, 34]

del second_list[1]

print(second_list)  # [11, 43, 64, 34]
