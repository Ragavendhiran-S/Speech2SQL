import sqlite3

connection = sqlite3.connect('student.db')
cursor = connection.cursor()

table_info = """
   CREATE TABLE STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT,
    MARKS INTEGER
);
"""
cursor.execute(table_info)
queries = [
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('John Doe', 'Science', 'A', 85);""",
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('Jane Smith', 'Mathematics', 'B', 78);""",
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('Alice Johnson', 'History', 'C', 90);""",
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('Bob Brown', 'English', 'A', 82);""",
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('Emily Davis', 'Science', 'B', 76);""",
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('Michael Wilson', 'Mathematics', 'C', 88);""",
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('Sophia Martinez', 'History', 'A', 95);""",
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('James Anderson', 'English', 'B', 79);""",
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('Olivia Taylor', 'Science', 'C', 84);""",
    """INSERT INTO STUDENT(NAME, CLASS, SECTION, MARKS) VALUES ('William Thomas', 'Mathematics', 'A', 91);"""
]

for query in queries:
    cursor.execute(query)


for row in cursor.execute('''select * from student'''):
   print(row)
connection.commit();
connection.close();