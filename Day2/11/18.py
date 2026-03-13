from math import *

for A in range(1, 1000):
    len_s = 261
    i = ceil(log2(A))
    v1 = ceil((len_s * i) / 8)
    v252_500 = v1 * 252_500
    if v252_500 > 31 * 1024 * 1024:
        print(A)