import csv
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

with open("students_import.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    records = [
        (row["id"], row["name"], row["age"], row["marks"])
        for row in reader
    ]

cursor.executemany(
    "INSERT INTO students (id, name, age, marks) VALUES (?, ?, ?, ?)",
    records
)

connection.commit()
connection.close()
print("CSV data imported.")