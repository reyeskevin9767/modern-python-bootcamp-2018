
# * Using SQLLite
import sqlite3
conn = sqlite3.connect("my_friends.db")

# Create Cursor Object
c = conn.cursor()
# Exexute SQL
# c.execute(
# "CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER)")
# insert_query = """INSERT INTO friends
#                         VALUES ('Merriwether', 'Lewis', 7)"""

# form_first = "Mary-Todd"
data = ("Steve", "Irwin", 9)
query = f"INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)
# Commit Changes
conn.commit()
conn.close()
