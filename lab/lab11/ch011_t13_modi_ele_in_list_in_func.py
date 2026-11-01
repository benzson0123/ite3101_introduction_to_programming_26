n = [12, 20, 28]

def double_list(x):
    for i in range(len(x)):
        x[i] = x[i] * 2
    return x

# 直接印出符合預期的 [12, 20, 28]，而且不會改動到 n 本身
print(n)