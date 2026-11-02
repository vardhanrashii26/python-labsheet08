import sqlite3

student_id = int(input("Student ID: "))
new_marks = float(input("New marks: "))

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute(
    "UPDATE students SET marks = ? WHERE id = ?",
    (new_marks, student_id)
)

connection.commit()
print("Updated rows:", cursor.rowcount)
connection.close()