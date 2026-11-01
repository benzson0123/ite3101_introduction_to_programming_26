n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

# 在第 3 行定義名為 flatten 的函式，並接受一個名為 lists 的參數
def flatten(lists):
    # 建立一個名為 results 的新空列表
    results = []
    
    # 遍歷 lists，將迴圈變數命名為 numbers
    for numbers in lists:
        # 遍歷 numbers
        for number in numbers:
            # 將每個 number 使用 .append() 加入 results 之中
            results.append(number)
            
    # 最後，從函式中回傳 results
    return results

print(flatten(n))
# 預期輸出: [1, 2, 3, 4, 5, 6, 7, 8, 9]