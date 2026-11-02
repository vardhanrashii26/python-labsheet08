import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
SELECT age, COUNT(*)
FROM students
GROUP BY age
ORDER BY age
""")

for age, count in cursor.fetchall():
    print("Age:", age, "| Students:", count)

connection.close()