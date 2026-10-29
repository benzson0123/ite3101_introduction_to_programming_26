from typing import List

# Student data
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Create the students list
students = [lloyd, alice, tyler]

def average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers"""
    total = sum(numbers)
    return total / len(numbers)

def get_average(student: dict) -> float:
    """Calculate weighted average for a student"""
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score: float) -> str:
    """Convert numerical score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(class_list: List[dict]) -> float:
    """Calculate the average score for the entire class"""
    results = []
    for student in class_list:
        results.append(get_average(student))
    return average(results)

# Test the functions
print("Individual student grades:")
for student in students:
    avg = get_average(student)
    grade = get_letter_grade(avg)
    print(f"{student['name']}: {avg:.2f} -> {grade}")

print(f"\nClass average: {get_class_average(students):.2f}")
print(f"Class letter grade: {get_letter_grade(get_class_average(students))}")
Key changes made:

Added students = [lloyd, alice, tyler] list
Cleaned up the global declarations (not needed for the actual application)
Added docstrings for better documentation
Enhanced the output with formatted results
Expected output:

Copy code

Individual student grades:
Lloyd: 80.55 -> B
Alice: 91.15 -> A
Tyler: 79.90 -> C

Class average: 83.87
Class letter grade: B
The program now correctly:

Calculates weighted averages (10% homework, 30% quizzes, 60% tests)
Converts numerical scores to letter grades
Computes the class average
Properly displays all results

print(get_letter_grade(get_average(lloyd)))

# Add your function below!
def get_class_average(class_list: List[dict]) -> float:
    results = []
    for student in class_list:
        results.append(get_average(student))
    return average(results)

print(get_class_average(students))# Add code below!
