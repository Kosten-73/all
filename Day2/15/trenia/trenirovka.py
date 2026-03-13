# 1
# def DEL(n, m):
#     return n % m == 0
#
#
# for A in range(1, 10000):
#     # a_ans = True
#     for x in range(1, 10000):
#         if not ((not (DEL(x, A))) <= ((not (DEL(x, 18))) or (not (DEL(x, 42))))):
#             # a_ans = False
#             break
#     # if a_ans:
#     #     print(A)
#     else:
#         print(A)

# 2
# for A in range(1, 10_000):
#     for x in range(1, 10_000):
#         if not ((x & 34 != 0) <= ((x & 41 == 0) <= (x & A != 0))):
#             break
#     else:
#         print(A)
#         break

# 3 Первое решение
# for A in range(1,1000):
#     for x in range(1, 1000):
#         for y in range(1, 1000):
#             if not(((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37)):
#                 break
#         if not (((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37)):
#             break
#     else:
#         print(A)
#         break
# 3 Второе решение
# for A in range(1, 1_000):
#     if all(((y + 5 * x != 31) or (A > x - 2)) and (A < y + 37)
#            for x in range(1, 1_000)
#            for y in range(1, 1_000)):
#         print(A)
#         break
# 4 Целые числа
# R = list(range(12, 31 + 1))
# Q = list(range(6, 15 + 1))
# P = list(range(17, 23 + 1))
# A = []
#
# for x in range(1, 1000):
#     if (((x in A) or (x in P)) or ((x in Q) <= (x in R))) == False:
#         print((((x in A) or (x in P)) or ((x in Q) <= (x in R))), x, A)
#         A.append(x)
#         print((((x in A) or (x in P)) or ((x in Q) <= (x in R))), x, A)
#
# print(A)
 # 6 = 6
 # 11 = 12
# [6, 12]
# 12 - 6 = 6
# 4 Вещественные числа
# R = [x / 10 for x in range(120, 310 + 1)]
# Q = [x / 10 for x in range(60, 150 + 1)]
# P = [x / 10 for x in range(170, 230 + 1)]
# A = []
#
# for x0 in range(10, 10_000):
#     x = x0 / 10
#     if not (((x in A) or (x in P)) or ((x in Q) <= (x in R))):
#         A.append(x)
#
# print(A)
# 5
Q = [x / 10 for x in range(80, 170 + 1)]
P = [x / 10 for x in range(30, 110 + 1)]
# Вот тут x / 10 надо было
A = [x / 10 for x in range(10, 10_000)]
for x0 in range(10, 10_000):
    x = x0 / 10
    if not (((x in A) <= (x in P)) or (x in Q)):
        A.remove(x)
print(A)

# Q = list(range(8, 17 + 1))
# P = list(range(3, 11 + 1))
# A = list(range(1, 100))
# for x in range(1, 100):
#     if not (((x in A) <= (x in P)) or (x in Q)):
#         A.remove(x)
# print(A)
