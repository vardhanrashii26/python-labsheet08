import sqlite3

try:
    connection = sqlite3.connect("school.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())

except sqlite3.Error as error:
    print("Database error:", error)

finally:
    if "connection" in locals():
        connection.close()