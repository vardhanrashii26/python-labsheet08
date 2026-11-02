import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM students WHERE marks < 40")

connection.commit()
print("Deleted rows:", cursor.rowcount)
connection.close()