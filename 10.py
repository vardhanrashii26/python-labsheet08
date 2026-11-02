import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")
for record in cursor.fetchall():
    print(record)

connection.close()