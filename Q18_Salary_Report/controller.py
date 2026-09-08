class SalaryController:

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

                    departments = self.model.get_departments()

                    if not departments:
                        print("No departments found.")
                        continue

                    self.view.display_departments(departments)

                    department = self.view.get_department()

                    employees = self.model.get_salary_report(
                        department
                    )

                    self.view.display_report(employees)

                elif choice == "3":

                    self.model.close()
                    print("Program ended.")
                    break

                else:
                    print("Invalid choice.")

            except Exception as e:
                print("Error:", e)
