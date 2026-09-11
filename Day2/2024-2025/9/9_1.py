f = open('9_lexa.txt')
k = 0
# for x in f:
#     a = [int(y) for y in (x.split())]
#     if 3 <= a.count(max(a)) <=4 and 5<= len(set(a))<=6:
#         nep = [y for y in a if a.count(y)==1]
#         if max(nep) + min(nep) <= sum(nep) - max(nep) - min(nep):
#             k += 1
for x in f:
    a = sorted([int(y) for y in (x.split())])
    a0 = [y for y in a if a.count(y) == 1]
    if (a.count(a[-1]) == 3 and len(a0) == 5) or (a.count(a[-1]) == 4 and len(a0) == 4):
        if a0[-1] + a0[0] <= sum(a0[1:-1]):
            k += 1
print(k)