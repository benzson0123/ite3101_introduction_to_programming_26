from typing import List

from typing import List

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x 

# 改為直接印出 range(3) 的串列
print(list(range(3)))