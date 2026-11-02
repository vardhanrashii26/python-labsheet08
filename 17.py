import sqlite3

student_id = int(input("Student ID: "))
new_name = input("New name: ")

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute(
    "UPDATE students SET name = ? WHERE id = ?",
    (new_name, student_id)
)

connection.commit()
print("Updated rows:", cursor.rowcount)
connection.close()