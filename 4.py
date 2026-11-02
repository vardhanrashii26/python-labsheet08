import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(students)")
for column in cursor.fetchall():
    print(column)

connection.close()