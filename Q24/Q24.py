import pandas as pd

# Load the dataset
df = pd.read_csv("titanic.csv")

print("ORIGINAL DATASET")
print("-" * 60)
print("Rows and Columns:", df.shape)
print("\nFirst 5 Records:")
print(df.head())

# Check missing values
print("\nMISSING VALUES BEFORE CLEANING")
print("-" * 60)
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing numerical values with median
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# Fill missing categorical values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Sex"] = df["Sex"].fillna(df["Sex"].mode()[0])

# Replace missing Cabin values
df["Cabin"] = df["Cabin"].fillna("Unknown")

# Fill missing text values
df["Name"] = df["Name"].fillna("Unknown")
df["Ticket"] = df["Ticket"].fillna("Unknown")

# Convert categorical columns into numerical form
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# Display missing values after cleaning
print("\nMISSING VALUES AFTER CLEANING")
print("-" * 60)
print(df.isnull().sum())

# Display cleaned dataset
print("\nCLEANED DATASET")
print("-" * 60)
print(df.head(10))

# Save cleaned dataset
df.to_csv("cleaned_titanic.csv", index=False)

print("\nDataset cleaning and preprocessing completed successfully.")
print("Cleaned file saved as: cleaned_titanic.csv")                       
