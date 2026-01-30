from itertools import product
s = product('АВЕ*****', repeat = 3)
cnt = 0
for x in s :
    y = ''.join(x)
    print(y)
    if y.count('В') == 1:
        cnt += 1
    if y.count('В') == 1 and y.count('А') == 0:
        print(cnt)
        break
