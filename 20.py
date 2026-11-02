import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM students")

connection.commit()
connection.close()
print("All student records deleted; table structure remains.")