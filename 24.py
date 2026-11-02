import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT AVG(marks) FROM students")
average = cursor.fetchone()[0]

print("Average marks:", average if average is not None else "No records")

connection.close()