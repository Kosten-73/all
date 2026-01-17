from itertools import *

cnt1 = 0
cnt2 = 0
for number, word in enumerate(product(sorted("ИНФОРМАТ"), repeat=5), start=1):
    # print(number, "".join(word))
    if number % 2 != 0 and word[0] != "О" and 1 <= word.count("Н") <= 2:
        cnt1 += 1
    if number % 2 != 0 and word[0] != "О" and (word.count("Н") == 1 or word.count("Н") == 2):
        cnt2 += 1
print(cnt1, cnt2)
