import sqlite3

student_id = int(input("Student ID to delete: "))

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

connection.commit()
print("Deleted rows:", cursor.rowcount)
connection.close()