from itertools import *

cnt = cnt2 = cnt3 = 0

for number, word in enumerate(permutations("0123456789", r=4), start=1):
    wordStr = "".join(word)
    wordStrRep = "".join(word)
    # print(word, word[0])
    if word[0] != "0":
        # 1
        wordReplace = (wordStr.replace("2", "0")
                       .replace("4", "0")
                       .replace("6", "0")
                       .replace("8", "0")
                       .replace("3", "1")
                       .replace("5", "1")
                       .replace("7", "1")
                       .replace("9", "1"))
        if "00" not in wordReplace and "11" not in wordReplace:
            cnt+=1
        # 2
        if word[0] != "0":
            for d in "2468":
                wordStrRep = wordStrRep.replace(d, "0")
            for d in "13579":
                wordStrRep = wordStrRep.replace(d, "1")
            if "00" not in wordReplace and "11" not in wordReplace:
                cnt2 += 1
        # print(number, word, wordStr)
        # 3
        if word[0] != "0" and int(word[0]) % 2 != int(word[1]) % 2 and \
                int(word[1]) % 2 != int(word[2]) % 2 and \
                int(word[2]) % 2 != int(word[3]) % 2:
            cnt3 += 1

print(cnt)
print(cnt2)
print(cnt3)