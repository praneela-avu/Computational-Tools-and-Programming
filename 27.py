import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the data
data = {
    "Student": ["S1", "S2", "S3", "S4", "S5",
                "S6", "S7", "S8", "S9", "S10"],
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    "Physics": [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    "Chemistry": [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    "English": [80, 84, 72, 91, 76, 80, 70, 95, 77, 89]
}

df = pd.DataFrame(data)

# Display data
print(df)

# 1. Subject-wise score distributions
sns.histplot(df["Mathematics"])
plt.title("Mathematics Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

sns.histplot(df["Physics"])
plt.title("Physics Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

sns.histplot(df["Chemistry"])
plt.title("Chemistry Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

sns.histplot(df["English"])
plt.title("English Score Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 2. Relationships between subjects
sns.pairplot(df.drop(columns="Student"))
plt.show()

# 3. Correlation heatmap
correlation = df.drop(columns="Student").corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Subject Scores")
plt.show()