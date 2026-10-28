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

total = 0

for key, price in prices.items():
    item_value = price * stock[key]
    print(item_value)
    total += item_value

    print("Total inventory value:", total)