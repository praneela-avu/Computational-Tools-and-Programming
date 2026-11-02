import matplotlib.pyplot as plt

# Student data
students = [
    "S1", "S2", "S3", "S4", "S5",
    "S6", "S7", "S8", "S9", "S10"
]

study_hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]

exam_scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

# Display data
print("STUDENT STUDY HOURS AND EXAM SCORES")
print("-" * 45)

for i in range(len(students)):
    print(
        students[i],
        "-> Study Hours:",
        study_hours[i],
        "Exam Score:",
        exam_scores[i]
    )

# Histogram of study hours
plt.figure(figsize=(8, 5))
plt.hist(study_hours, bins=5, edgecolor="black")

plt.title("Distribution of Students' Study Hours")
plt.xlabel("Study Hours per Week")
plt.ylabel("Number of Students")

plt.show()

# Histogram of exam scores
plt.figure(figsize=(8, 5))
plt.hist(exam_scores, bins=5, edgecolor="black")

plt.title("Distribution of Examination Scores")
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")

plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(study_hours, exam_scores, s=80)

plt.title("Study Hours vs Examination Score")
plt.xlabel("Study Hours per Week")
plt.ylabel("Exam Score")
plt.grid(True)

plt.show()