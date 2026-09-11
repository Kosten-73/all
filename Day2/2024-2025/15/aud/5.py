D = list(range(17, 58 + 1))
C = list(range(29, 80 + 1))
A = []

# print(D)
# print(C)

for x in range(1, 100):
    if not ((x in D) <= ((((not (x in C)) and (not (x in A))) <= (not (x in D))))):
        A.append(x)
print(A)

# 17 = 17
# 28 = 29
# [17, 29]
# 29 - 17 = 12
