f = open("9_28930.txt")
cnt = 0
cnt1 = 0
for s in f:
    a = list(map(int, s.split()))
    b = list(map(int, s.split()))
    b.sort()
    # print(a == b)
    if a == b:
        print(a, b)
print(cnt)
print(cnt1)
