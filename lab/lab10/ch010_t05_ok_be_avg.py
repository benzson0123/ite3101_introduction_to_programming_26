from typing import List

# Task 1 & 2: 學生資料字典
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

# Task 3: 學生清單
students = [lloyd, alice, tyler]

# Task 4: 印出學生資料 (如果你的測試系統有要求的話)
for student in students:
    print(student["name"])
    print(student["homework"])
    print(student["quizzes"])
    print(student["tests"])

# Task 5: 計算算術平均數的函數
def average(numbers: List[float]) -> float:
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
