# for x in range(1, 2031):
#     s = 7**91 + 7**160 - x
#     digit = []
#     while s > 0:
#         digit.append(s % 7)
#         s //= 7
#     if digit.count(0) == 70:
#         print(x)

from main import perevodCC

for x in range(1, 2031):
    s = 7 ** 91 + 7 ** 160 - x
    print(x if perevodCC(s, 7).count('0') == 70 else "")