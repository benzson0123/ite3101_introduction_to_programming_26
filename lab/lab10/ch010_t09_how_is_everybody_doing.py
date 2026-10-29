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
for s in students:  # Changed 'student' to 's'
    avg = get_average(s)
    grade = get_letter_grade(avg)
    print(f"{s['name']}: {avg:.2f} -> {grade}")   
print(f"\nClass average: {get_class_average(students):.2f}")
print(f"Class letter grade: {get_letter_grade(get_class_average(students))}")
