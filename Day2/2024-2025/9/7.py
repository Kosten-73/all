f = open("9_28930.txt")
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    povt = [x for x in a if a.count(x) > 1]
    ne_povt = [x for x in a if a.count(x) == 1]
    if len(povt) == 2 and (sum(ne_povt) / len(ne_povt)) <= (sum(povt)) :
        cnt += 1
print(cnt)