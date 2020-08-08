
# * Tricks With Slices
string = "This is fun!"

print(string[::-1])  # !nuf si sihT

numbers = [1, 2, 3, 4, 5]

numbers[1:3] = ['a', 'b', 'c']

print(numbers)  # [1, 'a', 'b', 'c', 4, 5]
