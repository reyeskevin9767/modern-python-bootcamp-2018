
# * Accessing All Values in a Dictionary
instructor = {
    'name': 'Colt',
    'owns_dog': True,
    'num_courses': 4,
    'favorite_language': 'Python',
    'is_hilarious': False,
    44: 'my favorite number!'
}


for value in instructor.values():
    print(value)

# "Colt"
# True
# 4
# "Python"
# False
# "my favorite number!"

for key in instructor.keys():
    print(key)

# name
# owns_dog
# num_courses
# favorite_language
# is_hilarious
# 44

for key, value in instructor.items():
    print(key, value)

# name "Colt"
# owns_dog True
# num_courses 4
# favorite_language "Python"
# is_hilarious False
# 44 "my favorite number!"
