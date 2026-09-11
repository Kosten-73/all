from math import *

# 8
# A = 52 + 10 + 963
# print(A)
# print(log2(A))
# print(ceil(7.75))
# i = ceil(log2(A))
# print(f"i = {i}")
# for len_s in range(1000):
#     v1 = ceil(len_s * i / 8)
#     v2000 = v1 * 2_000
#     if v2000 <= 693 * 1024:
#         print(f"len_s = {len_s}")

len_s = 261
for A in range(1, 1000):
    i = ceil(log2(A))
    v1 = ceil(len_s * i / 8)
    v252_500 = v1 * 252_500
    if v252_500 > 31 * 2**20:
        print(A)
