n = [12, 20, 28]

def double_list(x):
    for i in range(len(x)):
        x[i] = x[i] * 2
    return x

# 不要在此處呼叫會修改到 n 的 double_list(n)，否則測試讀取時數值會再加倍
# print(double_list(n)) 