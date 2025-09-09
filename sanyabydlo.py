import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Students(
    id INT PRIMARY_KEY,
    name VARCHAR (30),
    age INT,
    major VARCHAR (15)
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Courses(
    course_id INT PRIMARY_KEY,
    course_name VARCHAR(30),
    instructor VARCHAR(30))
""")