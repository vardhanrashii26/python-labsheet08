import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS students")

connection.commit()
connection.close()
print("students table deleted.")