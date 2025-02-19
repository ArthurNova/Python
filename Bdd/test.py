import sqlite3

conn = sqlite3.connect('bdd/ma_base.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")
conn.commit()

cursor.execute("""
INSERT INTO users(name, age) VALUES(?, ?)""", ("olivier", 30))

cursor.execute("""SELECT name, age FROM users""")
user1 = cursor.fetchone()
print(user1)
