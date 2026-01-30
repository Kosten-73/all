from itertools import *

str = "СВЕТЛАНА"
map = dict()
for now in str:
    if now in map:
        map[now] += 1
    else:
        map[now] = 1
print(map)

cnt = 0
cnt2 = 0
for number, word in enumerate(set(permutations("СВЕТЛАНА", r=8)), start=1):
    # print(number, "".join(word))
    wordStr = "".join(word)
    if word.count("С") == map["С"] and word.count("В") == map["В"] and word.count("Е") == map["Е"] and word.count("Т") == map["Т"] and \
        word.count("Л") == map["Л"] and word.count("А") == map["А"] and word.count("Н") == map["Н"] and \
            "СС" not in wordStr and "ВВ" not in wordStr and \
            "ЕЕ" not in wordStr and "ТТ" not in wordStr and \
            "ЛЛ" not in wordStr and "АА" not in wordStr and \
            "НН" not in wordStr:
        cnt += 1
        # print(number, "".join(word))
    if all(word.count(now) == map[now] and f"{now}{now}" not in "".join(word) for now in "СВЕТЛАН"):
        cnt2 += 1
print(cnt)
print(cnt2)

# q = 0
# sett = set()
# for i1 in 'СВЕТЛАНА':
#     for i2 in 'СВЕТЛАНА':
#         for i3 in 'СВЕТЛАНА':
#             for i4 in 'СВЕТЛАНА':
#                 for i5 in 'СВЕТЛАНА':
#                     for i6 in 'СВЕТЛАНА':
#                         for i7 in 'СВЕТЛАНА':
#                             for i8 in 'СВЕТЛАНА':
#                                 a = i1+i2+i3+i4+i5+i6+i7+i8
#                                 if a.count('А') == 2 and a.count('С') == 1 and a.count('В') == 1 and a.count('Е') ==1 and a.count('Т')==1 and a.count('Л') == 1 and a.count('Н') == 1:
#                                     if i1 != i2 and i2 != i3 and i3 != i4 and i4 != i5 and i5 != i6 and i6 != i7 and i7 != i8 and (not(a in sett)):
#                                         sett.add(a)
#                                         q += 1
# print(q)