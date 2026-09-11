cnt = 0
for line in open("9_28930.txt"):
    f_red = list(map(int, line.split()))
    pov = [x for x in f_red if f_red.count(x) > 1]
    not_pov = [x for x in f_red if f_red.count(x) == 1]
    if len(pov) == 2 and len(set(not_pov)) == 3 and \
            (sum(not_pov) / len(not_pov)) <= pov[0] * 2:
        cnt += 1

print(cnt)

# sum(pov)