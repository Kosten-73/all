f=open("9_28930.txt")
k=0
k1=0
for s in f:
    a=[int(x) for x in s.split()]
    if len(set(a)) < 5:
        povt_norm = [x for x in a if a.count(x) > 1]
        if ((sum(a)-sum(povt_norm)) % 2) != 0:
            k+=1
    povt = [x for x in a if a.count(x) > 1]
    no_povt = [x for x in a if a.count(x) == 1]
    if povt and sum(no_povt) % 2 != 0:
        k1 += 1
print(k, k1)
