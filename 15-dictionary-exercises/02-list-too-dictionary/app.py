
# * List to Dictionary Exercise
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

print(person)   # [['name', 'Jared'], ['job', 'Musician'], ['city', 'Bern']]
print(answer)   # {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}
