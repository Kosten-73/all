f = open("9_28930.txt")
cnt = 0
cnt1 = 0
for s in f:
    a = list(map(int, s.split()))
    if (min(a) * 5 < (sum(a) - min(a)) and
            (a[0] * a[-1] == a[1] * a[2] or a[0] * a[1] == a[2] * a[-1] or a[0] * a[2] == a[1] * a[-1])):
        cnt += 1
    # b = list(map(int, s.split()))
    # b.sort()
    # if min(a) * 5 < (sum(a) - min(a)) and a[0] * a[-1] == a[1] * a[2]:
    #     cnt1 += 1

print(cnt)
print(cnt1)
