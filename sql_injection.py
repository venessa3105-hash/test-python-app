import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

user_input = input("ID: ")

cursor.execute(
    "SELECT * FROM users WHERE id = ?",
    (user_input,)
)
