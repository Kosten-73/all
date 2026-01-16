from itertools import *

cnt = 0
for number, word in enumerate(product(sorted("12345678"), repeat=5), start=1):
    print(number, "".join(word))
    if word.count("2") == 1:
        cnt += 1
print(cnt)
