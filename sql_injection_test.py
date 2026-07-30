import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

user_input = input("Enter ID: ")

query = f"SELECT * FROM users WHERE id = {user_input}"

cursor.execute(query)
