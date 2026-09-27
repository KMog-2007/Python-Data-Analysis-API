import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/student_performance.csv")

# Data cleaning
df = df.drop_duplicates()

df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Basic analysis
total_students = len(df)
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()
average_attendance = df["Attendance"].mean()

top_student = df.loc[df["Marks"].idxmax(), "Name"]

department_analysis = (
    df.groupby("Department")["Marks"]
    .mean()
    .sort_values(ascending=False)
)

# Display report
print("===== STUDENT PERFORMANCE REPORT =====")
print("Total Students:", total_students)
print("Average Marks:", round(average_marks, 2))
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Attendance:", round(average_attendance, 2), "%")
print("Top Performing Student:", top_student)

print("\nAverage Marks by Department:")
print(department_analysis)

# Visualization 1
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Name", y="Marks")
plt.title("Student Performance")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization 2
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Study_Hours",
    y="Marks",
    hue="Department"
)
plt.title("Study Hours vs Student Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# Generate report
report = f"""
========================================
STUDENT PERFORMANCE ANALYSIS REPORT
========================================

Total Students        : {total_students}
Average Marks         : {average_marks:.2f}
Highest Marks         : {highest_marks}
Lowest Marks          : {lowest_marks}
Average Attendance    : {average_attendance:.2f}%
Top Performing Student: {top_student}

Department-wise Average Marks
----------------------------------------
{department_analysis.to_string()}

========================================
End of Report
========================================
"""

with open("student_analysis_report.txt", "w") as file:
    file.write(report)

print("\nReport generated successfully.")
