from itertools import *

cnt = 0
for number, word in enumerate(permutations("ВИКАГОПТЕР", r=4), start=1):
    # print(number, "".join(word))
    if word[0] != "П" and "ГО" not in "".join(word):
        cnt += 1
print(cnt)
