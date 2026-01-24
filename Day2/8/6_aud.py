from itertools import *

cnt1 = 0
cnt2 = 0
for number, word in enumerate(permutations("ВИКАГОПТЕР", r=4), start=1):
    if word[0] != "П" and "ГО" not in "".join(word):
        cnt1 += 1
        print(number, "".join(word))

print(cnt1)
print(cnt2)
