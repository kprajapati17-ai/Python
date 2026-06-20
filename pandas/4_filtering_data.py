import pandas as pd

marks = {
    "Amit": 85,
    "Neha": 91,
    "Rahul": 78,
    "Priya": 95,
    "Karan": 88
}

students = pd.Series(marks, name="Marks")

print(students)

print("Top Student :", students.idxmax())
print("Highest Marks :", students.max())

print("Average :", students.mean())

print(students[students >= 90])