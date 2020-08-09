
# * Using SQLLite

import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()

people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)]


# c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

# for person in people:
#     c.execute("INSERT INTO friends VALUES (?,?,?)", person)
#     print("INSERTING NOW!!!")

average = 0
for person in people:
    c.execute("INSERT INTO friends VALUES (?,?,?)", person)
    average += person[2]

print(average/len(people))

# c.execute(query, data)
conn.commit()
conn.close()
