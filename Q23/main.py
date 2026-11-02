import xml.etree.ElementTree as ET

# Read existing XML file
tree = ET.parse("students.xml")
root = tree.getroot()

# Display existing student records
print("STUDENT INFORMATION")
print("-" * 70)

for student in root.findall("student"):
    print("ID:", student.get("id"))
    print("Name:", student.find("name").text)
    print("Department:", student.find("department").text)
    print("Year:", student.find("year").text)
    print("Email:", student.find("email").text)
    print("CGPA:", student.find("cgpa").text)
    print("-" * 70)

# Modify CGPA of student 101
for student in root.findall("student"):
    if student.get("id") == "101":
        student.find("cgpa").text = "8.5"

# Add a new student
new_student = ET.SubElement(root, "student", id="111")

ET.SubElement(new_student, "name").text = "Kiran Das"
ET.SubElement(new_student, "department").text = "CSE"
ET.SubElement(new_student, "year").text = "2"
ET.SubElement(new_student, "email").text = "kiran.das@example.com"
ET.SubElement(new_student, "cgpa").text = "8.8"

# Generate modified XML file
tree.write("modified_students.xml", encoding="utf-8", xml_declaration=True)

print("\nXML file modified successfully.")
print("New student added with ID: 111")
print("CGPA of student 101 modified to 8.5")
print("Generated file: modified_students.xml")
