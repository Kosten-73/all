# from random import randint
#
# # print(randint(1,8))
#
# x = randint(1,8)
# # print(x)
# while x != 3 and x != 4:
#     x = randint(1, 8)
#     # print(x)
# print(x)
# # print("x y w z")
# # for x in range(2):
# #     for y in range(2):
# #         for w in range(2):
# #             for z in range(2):
# #                 if (not ((x <= w) <= (w == z)) and y):
# #                     print(x, y, w, z)
#
# def f(n):
#     s = ''
#     while n:
#         s = str(n % 3) + s
#         n //= 3
#     return s
#
# for n in range(1, 1000):
#     n3 = f(n)
#     if n % 3 == 0:
#         n3 = '1' + n3 + '02'
#     else:
#         n3 += f((n % 3) * 5)
#     r = int(n3, 3)
#     if r >= 177:
#         print(n)
#         break
#
# print(f(3))

v1 =1024*768*30
v2 =800*600*28
print(v1,v2)
x = v1 -v2
print(x)
x100 = x*100
print(x100 / 2**13)

123937





