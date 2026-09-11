from itertools import *

cnt = 0
for number, word in enumerate(set(permutations("КАРЕТА", r=4)), start=1):
    # print(number, "".join(word))
    if "АА" not in "".join(word):
        cnt += 1
        print(number, "".join(word))
print(cnt)
