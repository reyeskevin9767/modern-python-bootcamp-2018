
# * Insert
first_list = [1, 2, 3, 4]

first_list.insert(2, 'Hi!')

print(first_list)  # [1, 2, 'Hi!', 3, 4]

# * Insert
first_list.insert(-1, 'The end!')

print(first_list)  # [1, 2, 'Hi!', 3, 'The end!', 4]

# * Insert
first_list.insert(4, 'Hello')

print(first_list)  # [1, 2, 'Hi!', 3, 'Hello', 'The end!', 4]
