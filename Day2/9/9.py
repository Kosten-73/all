f = open("9_28930.txt")
cnt = 0
for s in f:
    a = list(map(int, s.split()))
    chet = [x for x in a if x % 2 == 0]
    no_chet = [x for x in a if x % 2 != 0]
    if (len(set(a)) == 5 and
            len(chet) < len(no_chet) and
            sum(chet) > sum(no_chet)):
        cnt += 1
print(cnt)
