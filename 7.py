import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
SELECT name FROM sqlite_master
WHERE type = 'table' AND name = ?
""", ("students",))

print("Table exists." if cursor.fetchone() else "Table does not exist.")
connection.close()