
# * Exercise
'''
print_users() # None
# prints to the console:
# Colt Steele
'''


from csv import DictReader


def print_users():
    with open("users.csv") as csvfile:
        csv_reader = DictReader(csvfile)
        for row in csv_reader:
            # each row is an OrderedDict!
            print(row['First Name'] + " " + row['Last Name'])


print_users()

# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_readers)
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")
