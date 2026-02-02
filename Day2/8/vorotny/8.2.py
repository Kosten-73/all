from itertools import *
alf='01234567'
k=0
for x in product(alf, repeat=5):
    s=''.join(x)
    if s[0]!='0':
        s = s.replace('3', '1').replace('5', '1').replace('7', '1')
        if s.count('6')==1 and '61' not in s and '16' not in s:
            k+=1
print(k)