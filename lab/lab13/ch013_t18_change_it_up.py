fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!')  # (It actually is.)
        # 👈 把這裡的 break 刪除，讓程式可以繼續往下走
    print('A', f)
else:
    print('A fine selection of fruits!')
