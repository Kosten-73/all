# print("x y z")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             if not((x == z) or (x <= (y and z))):
#                 print(x, y, z)
a = 19
b = 33
k = 0
k_while = 0
for i in range(a, b):
    if i % 2 == 0:
        k += 1
        print(i)
while a < b:
    if a % 2 == 0:
        k_while += 1
        print(a)
    a += 1

print(k_while)
