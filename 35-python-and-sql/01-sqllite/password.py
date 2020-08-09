
# * Using SQLLite
import sqlite3
conn = sqlite3.connect("users.db")

# query = "CREATE TABLE users (username TEXT, password TEXT)"

u = input("Please enter your username...")
p = input("Please enter your password...")
# query = f"SELECT * FROM users WHERE username ='{u}' and password = '{p}'"

query = f"SELECT * FROM users WHERE username =? and password =?"

c = conn.cursor()
c.execute(query, (u, p))

result = c.fetchone()
if (result):
    print("Welcome Back")
else:
    print("Failed LOGIN")


conn.commit()
conn.close()
