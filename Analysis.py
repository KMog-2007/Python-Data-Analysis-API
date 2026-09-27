import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("data/Student_Performance.csv")

print("===== STUDENT PERFORMANCE REPORT =====")

# ==========================================
# 2. DATA CLEANING
# ==========================================

df = df.drop_duplicates()

df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# ==========================================
# 3. DATA ANALYSIS
# ==========================================

total_students = len(df)
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()
average_attendance = df["Attendance"].mean()

top_student = df.loc[df["Marks"].idxmax(), "Name"]

department_analysis = df.groupby("Department")["Marks"].mean()

print("Total Students:", total_students)
print("Average Marks:", round(average_marks, 2))
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
print("Average Attendance:", round(average_attendance, 2), "%")
print("Top Performing Student:", top_student)

print("\nAverage Marks by Department:")
print(department_analysis)

# ==========================================
# 4. MATPLOTLIB VISUALIZATION
# ==========================================

plt.figure(figsize=(10, 5))

plt.bar(df["Name"], df["Marks"])

plt.title("Student Performance")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# 5. SEABORN VISUALIZATION
# ==========================================

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

# ==========================================
# 6. REST API AND JSON
# ==========================================

print("\n===== REST API TEST =====")

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("API Status Code:", response.status_code)

if response.status_code == 200:

    users = response.json()

    print("Number of users received:", len(users))

    print("\nFirst API User:")
    print("Name:", users[0]["name"])
    print("Email:", users[0]["email"])

else:
    print("API request failed.")

# ==========================================
# 7. GENERATE REPORT
# ==========================================

report = f"""
========================================
STUDENT PERFORMANCE ANALYSIS REPORT
========================================

Total Students         : {total_students}
Average Marks          : {average_marks:.2f}
Highest Marks          : {highest_marks}
Lowest Marks           : {lowest_marks}
Average Attendance     : {average_attendance:.2f}%
Top Performing Student : {top_student}

Department-wise Average Marks
----------------------------------------
{department_analysis.to_string()}

========================================
REST API INFORMATION
========================================

API Status Code        : {response.status_code}

========================================
End of Report
========================================
"""

with open("student_analysis_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

print("\n========================================")
print("STUDENT ANALYSIS REPORT GENERATED!")
print("File: student_analysis_report.txt")
print("========================================")
