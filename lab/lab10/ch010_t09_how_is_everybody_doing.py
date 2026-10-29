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

# 1. Create a list called students and fill it with the three students
students = [alice, lloyd, tyler]

def average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers"""
    return sum(numbers) / len(numbers)

def get_average(student: dict) -> float:
    """Calculate weighted average for a student"""
    homework = sum(student["homework"]) / len(student["homework"])
    quizzes = sum(student["quizzes"]) / len(student["quizzes"])
    tests = sum(student["tests"]) / len(student["tests"])
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
    return sum(results) / len(results)

# 2. Calculate and print the class average mark
print(get_class_average(students))