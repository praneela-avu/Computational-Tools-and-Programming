student1 = ("S1", "Alice", "CSE")
student2 = ("S2", "Bob", "ECE")

course1 = {"Python", "DSA", "DBMS"}
course2 = {"DSA", "DBMS", "Computer Networks"}

print("Student 1 details:", student1)
print("Student 2 details:", student2)

print("\nUnion:")
print(course1.union(course2))

print("\nIntersection:")
print(course1.intersection(course2))

print("\nCourses only in Student 1:")
print(course1.difference(course2))

print("\nCourses only in Student 2:")
print(course2.difference(course1))