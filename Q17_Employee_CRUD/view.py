class EmployeeView:

    def display_menu(self):
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

    def get_employee_details(self):

        employee_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        designation = input("Enter Designation: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))

        return employee_id, name, designation, department, salary

    def get_employee_id(self):
        return int(input("Enter Employee ID: "))

    def display_employees(self, employees):

        if not employees:
            print("No employee records found.")
            return

        print("\nID\tName\tDesignation\tDepartment\tSalary")
        print("-" * 70)

        for employee in employees:
            print(
                employee[0], "\t",
                employee[1], "\t",
                employee[2], "\t",
                employee[3], "\t",
                employee[4]
            )