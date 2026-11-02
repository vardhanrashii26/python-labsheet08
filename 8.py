import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
    (1, "Asha", 17, 89.5)
)

connection.commit()
connection.close()