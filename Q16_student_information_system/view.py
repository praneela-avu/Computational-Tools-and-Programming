class StudentView:

    def display_menu(self):
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

    def get_student_details(self):
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        cgpa = float(input("Enter CGPA: "))

        return roll_no, name, department, cgpa

    def display_students(self, students):

        if not students:
            print("No student records found.")
            return

        print("\nRoll No\tName\tDepartment\tCGPA")
        print("-" * 50)

        for student in students:
            print(
                student[0],
                "\t", student[1],
                "\t", student[2],
                "\t", student[3]
            )