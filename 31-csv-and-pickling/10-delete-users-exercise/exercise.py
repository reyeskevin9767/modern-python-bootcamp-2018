
# * Exercise
from csv import reader, writer

import csv


def delete_users(new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == new_first and row[1] == new_last:
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users deleted: {}.".format(count)


print(delete_users("Grace", "Hopper"))
