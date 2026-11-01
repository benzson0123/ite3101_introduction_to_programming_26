n = [12, 20, 28]

def double_list(x):
    for i in range(len(x)):
        x[i] = x[i] * 2
    return x

print(double_list(n))