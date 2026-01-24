from itertools import *

cnt1 = 0
cnt2 = 0
for number, word in enumerate(product(sorted("0123456789AB"), repeat=5), start=1):
    # 1
    if word[0] != "0" and word.count("7") == 1 and (word.count("9") + word.count("A") + word.count("B") <= 3):
        cnt1 += 1
    # 2
    if word[0] != "0" and word.count("7") == 1 and sum(1 for d in word if d >= "9") <= 3:
        cnt2 += 1
print(cnt1)
print(cnt2)
print("9" < "A")
print("9" < "a")
print("a" < "b")