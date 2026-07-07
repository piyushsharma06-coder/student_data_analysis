import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("student_data.csv")

# Display dataset
print("Student Data:")
print(df)

# Calculate average of Math marks
average_math = df["Math"].mean()

print("\nAverage Math Marks:", average_math)

# -------------------------
# BAR CHART
# -------------------------

plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Math"])

plt.title("Math Marks of Students")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()

# -------------------------
# SCATTER PLOT
# -------------------------

plt.figure(figsize=(8,5))

plt.scatter(df["Math"], df["Science"])

plt.title("Math vs Science")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")

plt.show()

# -------------------------
# HEATMAP
# -------------------------

plt.figure(figsize=(6,4))

numeric_data = df[["Math","Science","English"]]

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()
