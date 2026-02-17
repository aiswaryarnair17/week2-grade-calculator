# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Author: Aiswarya Nair

import os

# =========================
# Grade Calculation
# =========================

def calculate_grade(average):
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You\'re doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'


# =========================
# Input Validation
# =========================

def get_valid_number(prompt, min_val=0, max_val=100):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Enter value between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Enter numeric value.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Enter a positive number!")
        except ValueError:
            print("Invalid input! Enter a whole number.")


# =========================
# Display Functions
# =========================

def display_results(student_names, student_results):
    print("\n" + "=" * 60)
    print("                    RESULTS SUMMARY")
    print("=" * 60)
    print(f"{'Name':<20} | {'Avg':>6} | {'Grade':^6} | Comment")
    print("-" * 70)

    for i in range(len(student_names)):
        name = student_names[i]
        avg = student_results[i]['average']
        grade = student_results[i]['grade']
        comment = student_results[i]['comment']

        print(f"{name:<20} | {avg:>6.1f} | {grade:^6} | {comment}")


def display_statistics(student_names, student_results):
    averages = [result['average'] for result in student_results]

    class_avg = sum(averages) / len(averages)
    max_avg = max(averages)
    min_avg = min(averages)

    max_index = averages.index(max_avg)
    min_index = averages.index(min_avg)

    print("\n" + "=" * 60)
    print("                  CLASS STATISTICS")
    print("=" * 60)
    print(f"Total Students: {len(student_names)}")
    print(f"Class Average: {class_avg:.1f}")
    print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]})")
    print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]})")


# =========================
# Search Feature
# =========================

def search_student(student_names, student_results):
    name = input("Enter student name to search: ")
    if name in student_names:
        index = student_names.index(name)
        result = student_results[index]
        print(f"\n{name} - Average: {result['average']:.1f}, Grade: {result['grade']}")
    else:
        print("Student not found!")


# =========================
# Save to File
# =========================

def save_to_file(student_names, student_results):
    with open("results_sample.txt", "w") as file:
        file.write("Student Grade Results\n")
        file.write("=" * 50 + "\n")

        for i in range(len(student_names)):
            file.write(f"{student_names[i]} - ")
            file.write(f"Avg: {student_results[i]['average']:.1f}, ")
            file.write(f"Grade: {student_results[i]['grade']}\n")

    print("Results saved to results_sample.txt")


# =========================
# Main Program
# =========================

def main():
    print("=" * 60)
    print("           STUDENT GRADE CALCULATOR")
    print("=" * 60)

    num_students = get_positive_integer("Enter number of students: ")

    student_names = []
    student_results = []

    for i in range(num_students):
        print(f"\n=== STUDENT {i+1} ===")

        name = input("Student Name: ").strip()
        while name == "":
            print("Name cannot be empty!")
            name = input("Student Name: ").strip()

        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)

        student_names.append(name)
        student_results.append({
            'average': average,
            'grade': grade,
            'comment': comment
        })

    display_results(student_names, student_results)
    display_statistics(student_names, student_results)

    # Menu Options
    while True:
        print("\nMenu Options:")
        print("1. Search Student")
        print("2. Save Results to File")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            search_student(student_names, student_results)
        elif choice == "2":
            save_to_file(student_names, student_results)
        elif choice == "3":
            print("Exiting Program. Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
