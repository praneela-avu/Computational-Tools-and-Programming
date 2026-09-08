class SalaryView:

    def display_menu(self):

        print("\n===== SALARY REPORT SYSTEM =====")
        print("1. Add Employee")
        print("2. Generate Department Report")
        print("3. Exit")

    def get_employee_details(self):

        employee_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        return employee_id, name, department, salary

    def display_departments(self, departments):

        print("\nDepartments:")

        for department in departments:
            print(department)

    def get_department(self):

        return input("Enter Department: ")

    def display_report(self, employees):

        if not employees:
            print("No employees found.")
            return

        print("\n===== DEPARTMENT SALARY REPORT =====")

        print("ID\tName\tDepartment\tSalary")
        print("-" * 50)

        total = 0

        for employee in employees:

            print(
                employee[0], "\t",
                employee[1], "\t",
                employee[2], "\t",
                employee[3]
            )

            total += employee[3]

        print("-" * 50)
        print("Total Salary:", total)