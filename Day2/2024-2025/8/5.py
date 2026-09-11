from itertools import *

cnt1 = 0
cnt2 = 0
for number, word in enumerate(product(sorted("0123456789АВ"), repeat=5), start=1):
    # print(number, "".join(word))
    wordStr = "".join(word)
    # 1
    if word[0] != "0" and word.count("7") == 1 and \
        (word.count("9") + word.count("А") + word.count("В") <= 3):
        cnt1 += 1
    # 2
    if word[0] != "0" and word.count("7") == 1 and \
            sum(1 for d in word if d > "8") <= 3:
        cnt2 += 1
print(cnt1)
print(cnt2)
print("А" > "8")
print("а" > "8")
