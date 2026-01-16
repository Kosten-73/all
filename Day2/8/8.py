from itertools import *

cnt1 = 0
cnt2 = 0
cnt3 = 0
for number, word in enumerate(permutations("0123456789", r=4), start=1):
    # print(number, "".join(word))
    wordStr3 = "".join(word)
    # 1
    if word[0] != "0" and int(word[0]) % 2 != int(word[1]) % 2 and \
        int(word[1]) % 2 != int(word[2]) % 2 and \
        int(word[2]) % 2 != int(word[3]) % 2:
        cnt1 += 1
    # 2
    if word[0] != "0":
        wordStr = ("".join(word)
                   .replace("2", "0")
                   .replace("4", "0")
                   .replace("6", "0")
                   .replace("8", "0")
                   .replace("3", "1")
                   .replace("5", "1")
                   .replace("7", "1")
                   .replace("9", "1"))
        if "00" not in wordStr and "11" not in wordStr:
            cnt2 += 1
    # 3
    if word[0] != "0":
        for d in "2468":
            wordStr3 = wordStr3.replace(d, "0")
        for d in "3579":
            wordStr3 = wordStr3.replace(d, "1")
        if "00" not in wordStr3 and "11" not in wordStr3:
            cnt3 += 1

print(cnt1)
print(cnt2)
print(cnt3)
