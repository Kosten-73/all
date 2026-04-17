# x = "1" * 81
#
# while "11111" in x or "888" in x:
#     # if "11111" in x:
#     #     x = x.replace("11111", "88", 1)
#     # else:
#     #     x = x.replace("888", "8", 1)
#     x = x.replace("11111", "88", 1) if "11111" in x else x.replace("888", "8", 1)
#
# print(x)

# w = "111111111111111111111"
# print(w.replace("11111","88", 1))
# # # 881111111111111111

# x = "2" + "5" * 103
#
# while "25" in x or "2" in x:
#     if "25" in x:
#         x = x.replace("25", "552", 1)
#     else:
#         x = x.replace("2", "555", 1)
# print(x.count("5"))

# x = "1" + "0" * 90
# while "1" in x:
#     if "10" in x:
#         x = x.replace("10", "0001", 1)
#     else:
#         x = x.replace("1", "000", 1)
# print(x.count("0"))

# s = "3" * 9 + "2" * 22
# while "333" in s or "222" in s:
#     while "333" in s:
#         s = s.replace("333", "2", 1)
#     while "222" in s:
#         s = s.replace("222", "3", 1)
# print(s)

# s =  "3" * 60 + "2" * 60 + "1" * 60
# while "21" in s or "31" in s or "23" in s:
#     if "21" in s:
#         s = s.replace("21", "12", 1)
#     if "31" in s:
#         s = s.replace("31", "13", 1)
#     if "23" in s:
#         s = s.replace("23", "32", 1)
# print(s[12], s[112], s[172])

# for x in range(91, 10_000):
#     s = "3" * x
#     while "333" in s:
#         s = s.replace("333", "1", 1)
#         s = s.replace("111", "3", 1)
#     if s == "133":
#         print(s, x)
#         # break

# for n in range(4, 10_000):
#     s = "3" + "1" * n
#     while "31" in s or "211" in s or "1111" in s:
#         if "31" in s:
#             s = s.replace("31", "1", 1)
#         if "211" in s:
#             s = s.replace("211", "13", 1)
#         if "1111" in s:
#             s = s.replace("1111", "2", 1)
#     # a = [int(i) for i in s]
#     # if sum(a) == 15:
#     #     print(n, sum(a), a)
#     #     break
#     suma = sum(map(int, s))
#     # print(suma, *map(int, s))
#     if suma == 15:
#         print(n, suma)
#         break

def f(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1

for n in range(1, 1000):
    s= '>' + '0'*21 +'1' * n + '2' * 13
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1','22>', 1)
        if '>2' in s:
            s = s.replace('>2','2>', 1)
        if '>0' in s:
            s = s.replace('>0','1>', 1)
    # s = s.replace('>', '0')
    # a = sum([int(x) for x in s])
    b = s.count('1')+s.count('2')*2
    if f(b):
        print(n, b)






















