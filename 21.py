import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_name TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
""")

courses = [
    (1, 1, "Python"),
    (2, 2, "Mathematics"),
    (3, 3, "Science"),
]

cursor.executemany(
    "INSERT OR REPLACE INTO courses (course_id, student_id, course_name) VALUES (?, ?, ?)",
    courses
)

connection.commit()
connection.close()