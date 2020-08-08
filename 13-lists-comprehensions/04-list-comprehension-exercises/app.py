
# * List Conprehension Exercises
answer = [person[0] for person in ['Elie', 'Tim', 'Matt']]
print(answer)   # ['E', 'T', 'M']

answer_two = [val for val in [1, 2, 3, 4, 5, 6] if val % 2 == 0]
print(answer_two)  # [2, 4, 6]

answer_three = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]
print(answer_three)  # [3, 4]

# * the slice [::-1] is a quick way to reverse a string
answer_four = [val[::-1].lower() for val in ['Elie', 'Tim', 'Matt']]
print(answer_four)  # ['eile', 'mit', 'ttam']

answer_five = [val for val in range(1, 101) if val % 12 == 0]
print(answer_five)  # [12, 24, 36, 48, 60, 72, 84, 96]

answer_six = [char for char in 'amazing' if char not in 'aeiou']
print(answer_six)  # ['m', 'z', 'n', 'g']

answer_seven = [[i for i in range(0, 3)] for num in range(0, 3)]
print(answer_seven)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

answer_eight = [[i for i in range(0, 10)] for num in range(0, 10)]
print(answer_eight)
