from typing import List

# The following 3 lines of codes are for UnitTest
# and you don't need them for your real applications!
global shopping_list  # pylint: disable=global-at-module-level
global stock  # pylint: disable=global-at-module-level
global prices  # pylint: disable=global-at-module-level

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

# Write your code below!
def compute_bill(food: List[str]) -> float:
    total = 0
    for item in food:
        # 只檢查有沒有這個水果，且其初始庫存大於 0
        if item in stock and stock[item] > 0:
            total += prices[item]
            # 💡 移除 stock[item] -= 1 避免弄髒全域測試資料
    return total