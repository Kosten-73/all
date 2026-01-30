# from itertools import *
#
# str = "ГЕРАСИМ"
# map = dict()
# for now in str:
#     if now in map:
#         map[now] += 1
#     else:
#         map[now] = 1
# print(map)
#
# cnt = 0
# cnt2 = 0
# for number, word in enumerate((permutations("ГЕРАСИМ", r=7)), start=1):
#     # print(number, "".join(word))
#     wordStr = "".join(word)
#     # if word.count("Г") == map["Г"] and word.count("Е") == map["Е"] and word.count("Р") == map["Р"] and word.count("А") == map["А"] and \
#     #     word.count("С") == map["С"] and word.count("И") == map["И"] and word.count("М") == map["М"] and \
#     #         "ЕЕ" not in wordStr and "ЕА" not in wordStr and \
#     #         "ЕЕ" not in wordStr and "ТТ" not in wordStr and \
#     #         "ЛЛ" not in wordStr and "АА" not in wordStr and \
#     #         "НН" not in wordStr:
#     #     cnt += 1
#         # print(number, "".join(word))
#     if all(f"{now}{now}" not in "".join(word) for now in "ЕАИ") or \
#             all(f"{now}{now}" not in "".join(word) for now in "ГРСМ"):
#         cnt2 += 1
# print(cnt)
# print(cnt2)

import itertools
alphabet = "ГЕРАСИМ"
con = 'ГРСМ'
vol = 'ЕАИ'
ar = itertools.permutations(alphabet) #Перестановка
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    flag = True
    for i in range(len(e) - 1):
        if (e[i] in con and e[i + 1] in con) or (e[i] in vol and e[i + 1] in vol):
            flag = False
    if flag == True: count += 1
print(count)
