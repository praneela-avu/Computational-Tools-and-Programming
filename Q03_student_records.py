students = []


def insert_student():
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    department = input("Enter department: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Department": department
    }

    students.append(student)
    print("Student inserted successfully.")


def delete_student():
    roll = int(input("Enter roll number to delete: "))

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def search_student():
    roll = int(input("Enter roll number to search: "))

    for student in students:
        if student["roll"] == roll:
            print(student)
            return

    print("Student not found.")


while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        insert_student()

    elif choice == 2:
        delete_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        for student in students:
            print(student)

    elif choice == 5:
        break

    else:
        print("Invalid choice.")