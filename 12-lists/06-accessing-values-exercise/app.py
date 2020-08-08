
# * Accessing List Data Exercise
people = ['Hanna', 'Louisa', 'Claudia', 'Angela', 'Geoffrey', 'aparna']

# Change 'Hanna' to 'Hanna'
people[0] = 'Hannah'

# Change 'Geoffrey' to 'Jeffrey'
people[4] = 'Jeffrey'

# Change 'aparna' to 'Aparna' (capitalize it)
people[-1] = 'Aparna'

print(people)
# ['Hannah', 'Louisa', 'Claudia', 'Angela', 'Jeffrey', 'Aparna']

numbers = [1, 2, 3, 4]

for number in numbers:
    print(number)

# 1
# 2
# 3
# 4

numbers_two = [1, 2, 3, 4]
i = 0

while i < len(numbers_two):
    print(numbers_two[i])
    i += 1

# 1
# 2
# 3
# 4
