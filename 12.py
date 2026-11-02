import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students WHERE marks > ?", (80,))
for student in cursor.fetchall():
    print(student)

connection.close()