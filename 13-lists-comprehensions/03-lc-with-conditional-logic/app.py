
# * LC With Conditional Logic
numbers = [1, 2, 3, 4, 5, 6]

evens = [num for num in numbers if num % 2 == 0]
print(evens)  # [2, 4, 6]

odds = [num for num in numbers if num % 2 != 0]
print(evens)  # [2, 4, 6]

# * LC With Conditional Logic
module = [num*2 if num % 2 == 0 else num/2 for num in numbers]

print(module)   # [0.5, 4, 1.5, 8, 2.5, 12]

# * LC With Conditional Logic
with_vowels = 'This is so much fun!'

vowel = ''.join(char for char in with_vowels if char not in 'aeiou')

print(vowel)  # 'Ths s s mch fn!'
