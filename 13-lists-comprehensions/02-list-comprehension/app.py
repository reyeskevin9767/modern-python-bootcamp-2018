
# * List Comprehension
name = 'colt'

print([char.upper() for char in name])  # ['C', 'O', 'L', 'T']

# * List Comprehension
friends = ['ashley', 'matt', 'michael']

print([friend[0].upper() for friend in friends])  # ['A', 'M, 'M]

# * List Comprehension
print([num*10 for num in range(1, 6)])  # [10, 20, 30, 40, 50]

# * List Comprehension
print([bool(val) for val in [0, [], '']])  # [False, False, False]

# * List Comprehension
numbers = [1, 2, 3, 4, 5]

string_list = [str(num) for num in numbers]

print(string_list)  # ['1', '2', '3', '4', '5']
