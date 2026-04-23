import random
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   
def generate_data(n):
    students = []  # list

    for i in range(1, n + 1):
        student_id = f"S{i:03}"

        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        performance_index = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)
        students.append((student_id, marks, attendance, assignment, performance_index))
    return students

def classify_students(data):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for student in data:
        sid, marks, attendance, assignment, _ = student

        if marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)

        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)

        elif 71 <= marks <= 90:
            categories["Good"].append(sid)

        else:
            categories["Average"].append(sid)

    return categories

def analyze_data(df):
    marks_array = df["Marks"].values
    mean_marks = sum(marks_array) / len(marks_array)
    median_marks = np.median(marks_array)
    std_dev = np.std(marks_array)
    max_marks = np.max(marks_array)
    correlation = np.corrcoef(df["Marks"], df["Attendance"])[0][1]
    min_val = min(marks_array)
    max_val = max(marks_array)
    df["Normalized Marks"] = [
        (x - min_val) / (max_val - min_val) if max_val != min_val else 0
        for x in marks_array
    ]
    summary_tuple = (mean_marks, std_dev, max_marks)
    return mean_marks, median_marks, std_dev, correlation, summary_tuple

def system_insight(df, categories):
    std_dev = np.std(df["Marks"])
    low_attendance = [x for x in df["Attendance"] if x < 50]
    low_attendance_count = len(low_attendance)
    top_performers = len(categories["Top Performer"])
    if std_dev < 15 and top_performers >= 2:
        return "Stable Academic System"
    elif low_attendance_count > 3:
        return "Critical Attention Required"
    else:
        return "Moderate Performance"
if __name__ == "__main__":
    roll_last_digit = int(input("Enter last digit of roll number: "))
    n_students = max(10, roll_last_digit)
    data = generate_data(n_students)
    unique_ids = set([student[0] for student in data])
    df = pd.DataFrame(data, columns=[
        "Student_ID", "Marks", "Attendance", "Assignment", "Performance_Index"
    ])
    categories = classify_students(data)
    mean_marks, median_marks, std_dev, correlation, summary_tuple = analyze_data(df)
    insight = system_insight(df, categories)
    print("\n📊 DATAFRAME:\n")
    print(df)
    print("\n📂 CLASSIFICATION:\n")
    for k, v in categories.items():
        print(f"{k}: {v}")
    print("\n📈 STATISTICS:\n")
    print(f"Mean: {mean_marks:.2f}")
    print(f"Median: {median_marks:.2f}")
    print(f"Standard Deviation: {std_dev:.2f}")
    print(f"Correlation (Marks vs Attendance): {correlation:.2f}")
    print("\n📦 SUMMARY TUPLE:")
    print(summary_tuple)

    print("\n🧠 SYSTEM INSIGHT:")
    print(insight)
    plt.hist(df["Marks"], bins=5)
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()