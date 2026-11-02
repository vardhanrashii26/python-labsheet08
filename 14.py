import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM students")
print("Total students:", cursor.fetchone()[0])

connection.close()