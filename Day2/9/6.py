f = open("9_28930.txt")
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    povt = [x for x in a if a.count(x) > 1]
    ne_povt = [x for x in a if a.count(x) == 1]
    if (max(a) not in povt) and (len(ne_povt) == 3) and len(set(povt)) == 2:
        cnt += 1
print(cnt)