def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count += 1
    return count

# Example test:
print(fizz_count(["fizz", "cat", "fizz"])) 
