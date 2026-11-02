import sqlite3

def insert_student(student_id, name, age, marks):
    with sqlite3.connect("school.db") as connection:
        connection.execute(
            "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
            (student_id, name, age, marks)
        )

def fetch_students():
    with sqlite3.connect("school.db") as connection:
        return connection.execute("SELECT * FROM students").fetchall()

insert_student(10, "Neha", 17, 91)
for student in fetch_students():
    print(student)