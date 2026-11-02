import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses ON students.id = courses.student_id
""")

for row in cursor.fetchall():
    print(row)

connection.close()