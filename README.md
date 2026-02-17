## 📘 Student Grade Calculator

## 📌 Project Overview

The Student Grade Calculator is a Python-based console application that allows users to:

Enter student names and marks

Calculate individual averages

Assign grades

Display performance comments

Generate class statistics

This project demonstrates core Python programming concepts including input handling, loops, conditionals, functions, exception handling, and file operations.

## 🎯 Project Objectives

Store and process multiple students’ academic data

Calculate averages automatically

Assign grades based on performance

Display formatted results in a clean table layout

Compute overall class statistics

Handle invalid user inputs gracefully

## ⚙️ Setup & Installation Instructions
1️⃣ Install Python

Make sure Python 3.x is installed on your system.

Check using:

python --version

2️⃣ Clone the Repository
git clone (https://github.com/aiswaryarnair17/week2-grade-calculator)

3️⃣ Navigate to Project Folder
cd student-grade-calculator

4️⃣ Run the Program
python grade_calculator.py

## 🗂️ Code Structure
student-grade-calculator/
|
│
├── grade_calculator.py               # Main program file
|
├── README.md                         # Project documentation
|
├── test_students.txt                 # Sample input file
|
└── result_sample.txt                 # Saved output results

## Main Components:
Input Section:

Takes number of students

Collects name and subject marks

Validation:

Ensures marks are between 0–100

Uses try-except for error handling

Processing:

Calculates individual averages

Assigns grades (A, B, C, etc.)

Generates comments

Statistics:

Class average

Highest average

Lowest average

## 🖥️ Sample Program Output
===========================================
           STUDENT GRADE CALCULATOR
===========================================

Number of students: 3

=== STUDENT 1 ===
Name: John Smith
Math: 85
Science: 92
English: 88

=== STUDENT 2 ===
Name: Sarah Johnson
Math: 78
Science: 81
English: 85

===========================================
             RESULTS SUMMARY
===========================================

Name              | Avg  | Grade | Comment
------------------+------+-------+--------------
John Smith        | 88.3 | B     | Very Good!
Sarah Johnson     | 81.3 | B     | Very Good!

===========================================
            CLASS STATISTICS
===========================================

Total Students: 2
Class Average: 84.8
Highest Average: 88.3 (John Smith)
Lowest Average: 81.3 (Sarah Johnson)

## 🧠 Technical Implementation Details
1️⃣ Average Calculation

Each student's average is calculated as:

average = (math + science + english) / 3

2️⃣ Grade Assignment Logic

Example grading scale:

90+ → A

80–89 → B

70–79 → C

Below 70 → Needs Improvement

Implemented using if-elif-else statements.

3️⃣ Class Statistics

Used:

sum() for total average

max() to find highest average

min() to find lowest average

List comprehensions for cleaner calculations

## 🛠 Challenges & Solutions
🔹 Challenge 1: Handling Invalid Marks Input

Problem: User could enter non-numeric or out-of-range values
Solution:
Used while loop with try-except to validate input and ensure marks are between 0–100.

🔹 Challenge 2: Formatting the Results Table

Problem: Output looked misaligned
Solution:
Used string formatting with fixed width spacing:

f"{name:<18} | {avg:<5.1f} | {grade:<5}"

🔹 Challenge 3: Calculating Multiple Statistics

Problem: Needed class average, highest and lowest
Solution:
Used:

List comprehensions

Built-in functions (sum, max, min)

## 🧪 Testing Evidence
✅ Test Case 1 – Normal Input

Expected: Correct averages and statistics
Result: Passed

✅ Test Case 2 – Invalid Marks

Expected: Error message and re-entry prompt
Result: Passed

✅ Test Case 3 – Multiple Students

Expected: Correct class statistics
Result: Passed

## 🚀 Skills Demonstrated

Variables and Data Types

Loops (for, while)

Conditional Statements

Functions

Exception Handling

List Comprehensions

File Handling

String Formatting

Git & GitHub usage

Technical Documentation Writing

## 📌 Conclusion

This project successfully demonstrates foundational Python programming concepts and structured problem-solving. The application is user-friendly, validates input effectively, and presents results in a professional format.


