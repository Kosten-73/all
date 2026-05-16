# 1 задание
# s = 4096**210 - 1024**67 + 256**32 - 64
# print(s)
# # print("".join([str(i) for i in range(1, 2520)]))
# print(bin(s)[2:])
# print(bin(s)[2:].count('1'))

# # 2 задание
s = 9**8 + 3**24 - 3 * 7
# cnt2 = 0
# while s > 0:
#     if s % 3 == 2:
#         cnt2 += 1
#     s //= 3
#     print(s)
# print(cnt2)

# s1 = 9**8 + 3**24 - 3 * 7
# digits = []
# while s1 > 0:
#     digits.append(s1 % 3)
#     s1 //= 3
# print(digits.count(2))
# print(digits.count(0))
# print(digits.count(1))

from fun import F

# for x in range(2030, 0, -1):
# # for x in range(1, 2031):
#     s = 3**100 - x
#     r = s
#     cnt0 = 0
#     while s > 0:
#         if s % 3 == 0:
#             cnt0 += 1
#         s //= 3
#     if cnt0 == 5:
#         print(r, x)
#         # break






from fun import F

# for x in range(2030, 0, -1):
#     s = 7**91 + 7**160 - x
#     print(x if F(s, 7).count("0") == 70 else "")
    # cnt = 0
    # s1 = F(s, 7)
    # if s1.count("0") == 70:
    #     print(x)
    #     break
    # while s>0:
        # if s%7 == 0:
            # cnt += 1
    #     s //= 7
    # if cnt == 70:
    #     print(x)
    #     break

# def f(n):
#     k = 0
#     while n > 0:
#         if n % 25 > 10:
#             k += 1
#         n = n // 25
#     return k
#
#
# s = (4 * 3125 ** 2019 + 3 * 625 ** 2020 - 2 * 125 ** 2021
#      + 25 ** 2022 - 4 * 5 ** 2023 - 2024)
# print(f(s))


# s = (3 * 289 ** 2024 +
#      81 * 49 ** 121 -
#      9 * 16 ** 81 - 6011)
#
# summa = 0
# while s > 0:
#     if s % 31 <= 17:
#         summa += s % 31
#     s //= 31
# print(summa)




# for x in range(15):
#     n1 = int('97968015', 15) + x * 15 ** 2
#     n2 = int('70233', 15) + x * 15 ** 3
#     if (n1 + n2) % 14 == 0:
#         print((n1 + n2) // 14, x)

# for x in "0123456789ABCDE":
#     s = (int(f"97968{x}15", 15) +
#          int(f"7{x}233", 15))
#     if s % 14 == 0:
#         print(x, s)























from string import *

alt = digits + ascii_uppercase
print(alt)
print(alt[:19])
for x in alt[:19]:
    s = (int(f"98{x}79641", 19) +
         int(f"36{x}14", 19) +
         int(f"73{x}4" , 19))
    if s % 18 == 0:
        print(x , s // 18)





