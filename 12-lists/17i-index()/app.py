
# * Index
numbers = [5, 6, 7, 8, 9, 10]

print(numbers.index(6))  # 1
print(numbers.index(9)) # 4

# * Index
numbers_two = [5, 5, 6, 7, 5, 8, 8, 9, 10]

print(numbers_two.index(5)) # 0
print(numbers_two.index(5, 1))  # 1
print(numbers_two.index(5, 2))  # 4

print(numbers_two.index(8, 6, 8) ) # 6
