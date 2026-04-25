f=open("9_25348.txt")
k=0
for s in f :
    a=sorted([int(x) for x in s.split()])
    not_pov = [x for x in a if a.count(x) == 3]
    if len(not_pov) == 3 and len(set(a)) == 5:
        if a[-1] != a[-2]:
            k += 1
print(k)

