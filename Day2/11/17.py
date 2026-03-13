from math import *

# print(ceil(6.1))
# print(log2(100))
# print(ceil(log2(100)))

for len_s in range(1, 1000):
    A = 10 + 52 + 963
    i = ceil(log2(A))
    v1 = ceil((len_s * i) / 8)
    v2000 = v1 * 2000
    if v2000 <= 693 * 1024:
        print(len_s)
