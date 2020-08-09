
# * Exercise
'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

from csv import reader


def find_user(first_name, last_name):
    with open("users.csv") as file:
        csv_reader = reader(file)
        for (index, row) in enumerate(csv_reader):
            if row[0] == first_name and row[1] == last_name:
                return index

        return "{} {} not found.".format(first_name, last_name)


print(find_user("Grace", "Hopper"))

# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_readers)
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")
