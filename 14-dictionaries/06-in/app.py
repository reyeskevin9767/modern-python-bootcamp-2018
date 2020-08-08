
# * Dictionary In
instructor = {
    'name': 'Colt',
    'owns_dog': True,
    'num_courses': 4,
    'favorite_language': 'Python',
    'is_hilarious': False,
    44: 'my favorite number!'
}


print("name" in instructor)  # True
print("awesome" in instructor)  # False

print("Colt" in instructor.values()) # True
print("Nope!" in instructor.values() ) # False
