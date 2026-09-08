import sqlite3


class SalaryModel:

    def __init__(self):
        self.connection = sqlite3.connect("salary.db")
        self.create_table()

    def create_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        )
        """

        self.connection.execute(query)
        self.connection.commit()

    def add_employee(self, employee_id, name, department, salary):

        query = """
        INSERT INTO employees
        VALUES (?, ?, ?, ?)
        """

        self.connection.execute(
            query,
            (employee_id, name, department, salary)
        )

        self.connection.commit()

    def get_departments(self):

        query = "SELECT DISTINCT department FROM employees"

        cursor = self.connection.execute(query)

        return [row[0] for row in cursor.fetchall()]

    def get_salary_report(self, department):

        query = """
        SELECT employee_id, name, department, salary
        FROM employees
        WHERE department = ?
        """

        cursor = self.connection.execute(
            query,
            (department,)
        )

        return cursor.fetchall()

    def close(self):
        self.connection.close()
        