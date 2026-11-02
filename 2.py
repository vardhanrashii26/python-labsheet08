import sqlite3

connection = sqlite3.connect("new_database.db")
print("Database created successfully!")
connection.close()