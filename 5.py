import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("""
SELECT name FROM sqlite_master
WHERE type = 'table'
ORDER BY name
""")

for table in cursor.fetchall():
    print(table[0])

connection.close()