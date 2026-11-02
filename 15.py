import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
for student in cursor.fetchall():
    print(student)

connection.close()