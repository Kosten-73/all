from itertools import *
alf = sorted('ВЕРОНИКА')
k=0
for x in product(alf, repeat = 3):
    s = ''.join(x)
    if s.count('В')==1:
        k+=1
        if s.count('А')==0:
            break
print(k, s)