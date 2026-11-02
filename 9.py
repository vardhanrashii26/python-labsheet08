import sqlite3

records = [
    (2, "Ravi", 18, 76),
    (3, "Mina", 17, 93),
    (4, "Arjun", 18, 68),
]

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.executemany(
    "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
    records
)

connection.commit()
connection.close()