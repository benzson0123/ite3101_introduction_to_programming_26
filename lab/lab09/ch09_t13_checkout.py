
    total = 0
    for item in food:
        if item in stock and stock[item] > 0:
            total += prices[item]
    return total