class EmployeeController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):

        while True:

            self.view.display_menu()
            choice = input("Enter your choice: ")

            try:

                if choice == "1":

                    details = self.view.get_employee_details()
                    self.model.add_employee(*details)

                    print("Employee added successfully.")

                elif choice == "2":

                    employees = self.model.get_employees()
                    self.view.display_employees(employees)

                elif choice == "3":

                    employee_id = self.view.get_employee_id()

                    name = input("Enter New Name: ")
                    designation = input("Enter New Designation: ")
                    department = input("Enter New Department: ")
                    salary = float(input("Enter New Salary: "))

                    self.model.update_employee(
                        employee_id,
                        name,
                        designation,
                        department,
                        salary
                    )

                    print("Employee updated successfully.")

                elif choice == "4":

                    employee_id = self.view.get_employee_id()

                    self.model.delete_employee(employee_id)

                    print("Employee deleted successfully.")

                elif choice == "5":

                    self.model.close()
                    print("Program ended.")
                    break

                else:
                    print("Invalid choice.")

            except Exception as e:
                print("Error:", e)