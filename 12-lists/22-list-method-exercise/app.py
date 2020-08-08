
# * List Method Exercise
# * Create a list called instructors
instructors = []

# Add the following strings to the instructors list
# 'Colt'
# 'Blue'
# 'Lisa'

instructors.extend(['Colt', 'Blue', 'Lisa'])
print(instructors)  # ['Colt', 'Blue', 'Lisa']

# * Remove the last value in the list
instructors.pop()
print(instructors)  # ['Colt', 'Blue']


# * Remove the first value in the list
instructors.pop(0)
print(instructors)  # ['Blue']

# * Add the string 'Done' to the beginning of the list
instructors.insert(0, 'Done')
print(instructors)      # ['Done', 'Blue']
