
# * Dictionary Comprehension
numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key, value in numbers.items()}

print(squared_numbers)  # {'first': 1, 'second': 4, 'third': 9}

{num: num**2 for num in [1, 2, 3, 4, 5]}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}

print(combo)  # {'A': '1', 'B': '2', 'C': '3'}
