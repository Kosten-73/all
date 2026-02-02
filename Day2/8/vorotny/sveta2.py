from itertools import*
alf="СВЕТЛАНА"
k=0
for x in permutations(alf,r=8):
    s="".join(x)
    if len(set(s))==7 and s.count("А")==2:
        if "АА" not in s :
            k+=1
print(k)








# d = dict()
# d1 = dict()
# alf = "СВЕТЛАНА"
#
# for now in alf:
#     if now in d:
#         # d1[now] = [1, 4]
#         d[now] += 1
#     else:
#         d[now] = 1
# print(d)
# # d1['А'].append("2")
# # print(d1)
