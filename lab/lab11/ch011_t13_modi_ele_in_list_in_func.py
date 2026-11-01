n = [12, 20, 28]

def double_list(x):
    for i in range(len(x)):
        x[i] = x[i] * 2
    return x

# 請務必註解或刪除下面這行，否則測試時數值會被加倍兩次
# print(double_list(n))