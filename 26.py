import csv
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
columns = [description[0] for description in cursor.description]

with open("students_export.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(rows)

connection.close()
print("Data exported to students_export.csv")