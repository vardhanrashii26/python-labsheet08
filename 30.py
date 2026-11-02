import sqlite3

def show_students():
    with sqlite3.connect("school.db") as connection:
        rows = connection.execute("SELECT * FROM students").fetchall()
        for row in rows:
            print(row)

def add_student():
    student_id = int(input("ID: "))
    name = input("Name: ")
    age = int(input("Age: "))
    marks = float(input("Marks: "))

    with sqlite3.connect("school.db") as connection:
        connection.execute(
            "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
            (student_id, name, age, marks)
        )
    print("Student added.")

while True:
    print("\n1. Show students\n2. Add student\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_students()
    elif choice == "2":
        try:
            add_student()
        except (ValueError, sqlite3.Error) as error:
            print("Could not add student:", error)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")