from math import *
# наша длина пароля
N = 32
A = 10 + 240
i = ceil(log2(A))
print(f"i = {i} бит")
V1 = (N * i) / 8
print(f"v1 = {V1} байт")
V3200 = (V1 * 3_200) / 2**10
print(f"v3200 = {V3200} Кбайт")

# V = N * i
# V3200 = (32 * ceil(log2(10 + 240)) * 3_200) / 2**13
# print(f"v3200 = {V3200} Кбайт")