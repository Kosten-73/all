from itertools import *

cnt1 = 0
cnt2 = 0
for number, word in enumerate(product(sorted("012345678"), repeat=7), start=1):
    # print(number, "".join(word))
    wordStr = "".join(word)
    # 1
    if wordStr[0] != "0" and wordStr.count("5") == 1 and \
        "05" not in wordStr and "50" not in wordStr and \
        "25" not in wordStr and "52" not in wordStr and \
        "45" not in wordStr and "54" not in wordStr and \
        "65" not in wordStr and "56" not in wordStr and \
        "85" not in wordStr and "58" not in wordStr:
        cnt1 += 1
    # 2
    if wordStr[0] != "0" and wordStr.count("5") == 1 and \
            all(f"{d}5" not in wordStr and f"5{d}" not in wordStr for d in "02468"):
        cnt2 += 1

print(cnt1)
print(cnt2)
