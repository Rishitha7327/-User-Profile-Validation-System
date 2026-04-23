# Day 6 - Student Performance Analysis

This Python script simulates student performance data and provides analysis tools for educational assessment.

## Features

- **Data Generation**: Generates random student data including marks, attendance, and assignments.
- **Student Classification**: Categorizes students into performance levels (At Risk, Average, Good, Top Performer).
- **Data Analysis**: Computes statistical measures like mean, median, standard deviation, and correlation.

## Dependencies

Install the required packages using pip:

```
pip install -r requirements.txt
```

## Usage

Run the script in a Python environment:

```python
import Day-6

# Generate data for 100 students
students = generate_data(100)

# Classify students
categories = classify_students(students)

# For analysis, convert to DataFrame
import pandas as pd
df = pd.DataFrame(students, columns=['Student ID', 'Marks', 'Attendance', 'Assignment', 'Performance Index'])
analyze_data(df)
```

## Functions

- `generate_data(n)`: Generates data for n students.
- `classify_students(data)`: Classifies students based on marks and attendance.
- `analyze_data(df)`: Performs statistical analysis on a pandas DataFrame.

## Troubleshooting

- Ensure all dependencies are installed.
- Check Python version compatibility (tested on Python 3.x).
