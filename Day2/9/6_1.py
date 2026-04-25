cnt = 0
for line in open("9_28930.txt"):
    f_red = list(map(int, line.split()))
    pov = [x for x in f_red if  f_red.count(x) > 1]
    not_pov = [x for x in f_red if  f_red.count(x) == 1]
    if max(line) not in pov and len(not_pov) == 3 and len(set(pov)) == 2:
        cnt += 1
print(cnt)
# a = [13, 13, 13]
# print(a)
# print(set(a))