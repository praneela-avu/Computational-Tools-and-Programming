import sqlite3


class EmployeeModel:

    def __init__(self):
        self.connection = sqlite3.connect("employees.db")
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            designation TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        )
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_employee(self, employee_id, name, designation,
                     department, salary):

        query = """
        INSERT INTO employees
        VALUES (?, ?, ?, ?, ?)
        """

        self.connection.execute(
            query,
            (employee_id, name, designation, department, salary)
        )
        self.connection.commit()

    def get_employees(self):
        query = "SELECT * FROM employees"
        cursor = self.connection.execute(query)
        return cursor.fetchall()

    def update_employee(self, employee_id, name, designation,
                        department, salary):

        query = """
        UPDATE employees
        SET name = ?,
            designation = ?,
            department = ?,
            salary = ?
        WHERE employee_id = ?
        """

        self.connection.execute(
            query,
            (name, designation, department, salary, employee_id)
        )
        self.connection.commit()

    def delete_employee(self, employee_id):

        query = "DELETE FROM employees WHERE employee_id = ?"

        self.connection.execute(query, (employee_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()