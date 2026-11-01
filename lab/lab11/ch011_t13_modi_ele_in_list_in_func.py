n = [2, 3, 5]

def double_list(x):
    for i in range(len(x)):
        x[i] = x[i] * 2
    return x

print(double_list(n))