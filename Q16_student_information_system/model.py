import sqlite3


class StudentModel:

    def __init__(self):
        self.connection = sqlite3.connect("students.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students (
            roll_no INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            cgpa REAL NOT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_student(self, roll_no, name, department, cgpa):
        query = """
        INSERT INTO students
        VALUES (?, ?, ?, ?)
        """
        self.connection.execute(
            query,
            (roll_no, name, department, cgpa)
        )
        self.connection.commit()

    def get_students(self):
        query = "SELECT * FROM students"
        cursor = self.connection.execute(query)
        return cursor.fetchall()

    def close(self):
        self.connection.close()