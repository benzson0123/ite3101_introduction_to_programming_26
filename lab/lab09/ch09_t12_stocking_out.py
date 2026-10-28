from typing import List

shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
# Write your code below!
def compute_bill(food: List[str]) -> float: 
    total = 0
    for item in food:
        # 1. 確保水果在我們的價目表內
        # 2. 確保該水果目前還有庫存 (大於 0)
        if item in prices and stock[item] > 0:
            total += prices[item]
            stock[item] -= 1  # 成功購買，庫存減 1
    return total
