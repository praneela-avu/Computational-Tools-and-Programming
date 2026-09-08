class StudentController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):

        while True:

            self.view.display_menu()
            choice = input("Enter your choice: ")

            try:

                if choice == "1":
                    details = self.view.get_student_details()
                    self.model.add_student(*details)
                    print("Student added successfully.")

                elif choice == "2":
                    students = self.model.get_students()
                    self.view.display_students(students)

                elif choice == "3":
                    self.model.close()
                    print("Program ended.")
                    break

                else:
                    print("Invalid choice.")

            except Exception as e:
                print("Error:", e)