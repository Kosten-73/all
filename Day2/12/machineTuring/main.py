# x = 134_287
# x2 = 'h' + bin(x)[2:] + "hhhhhhhhh"
# print(x, x2)
# itog2 = ""
#
# def q0(x2, itog2):
#     for i in range(len(x2)):
#         if x2[i] == 'h':
#             itog2 += '1'
#             return q1(x2[i + 1:], itog2)
#
# def q1(x2, itog2):
#     for i in range(len(x2)):
#         if x2[i] == '0':
#             itog2 += '0'
#         if x2[i] == '1':
#             itog2 += '1'
#         if x2[i] == 'h':
#             itog2 += '0'
#             return q2(x2[i + 1:], itog2)
#
# def q2(x2, itog2):
#     for i in range(len(x2)):
#         if x2[i] == 'h':
#             itog2 += '1'
#             return q3(x2[i + 1:], itog2)
#
# def q3(x2, itog2):
#     for i in range(len(x2)):
#         if x2[i] == 'h':
#             itog2 += '0'
#             return itog2
#
# ans = q0(x2, itog2).replace('h', '')
# print(ans, int(ans, 2))

l = ['a']*20+list(bin(145682)[2:])+['a']*20
q = 0
p = 19
while True:
    if q == 0 and l[p] == 'a':
        l[p] = '1'
        p += 1
        q = 1
    if q == 1 and l[p] == 'a':
        l[p] = '0'
        p += 1
        q = 2
    if q == 1 and l[p] == '0':
        l[p] = '1'
        p += 1
    if q == 1 and l[p] == '1':
        l[p] = '0'
        p += 1
    if q == 2 and l[p] == 'a':
        l[p] = '0'
        p += 1
        q = 3
    if q == 3 and l[p] == 'a':
        l[p] = '1'
        break
print("".join([i for i in l if i != 'a']))
print(int('1011100011011101101001' , 2))
print(int('1100011100100010010001', 2))
