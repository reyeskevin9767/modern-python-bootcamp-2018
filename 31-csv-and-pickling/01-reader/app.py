# * Reader

from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        # each row is a list!
        print(row)


# from csv import reader
# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_readers)
#     next(csv_reader)
#     for fighter in csv_reader:
#         print(f"{fighter[0]} is from {fighter[1]}")


# from csv import reader
# with open("example.csv") as file:
#     csv_reader = reader(file, delimiter="|")
#     for row in csv_reader:
#         # each row is a list!
#         print(row)
