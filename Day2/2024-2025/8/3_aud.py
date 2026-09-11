from itertools import *

cnt = 0
for number, word in enumerate(product("01234567", repeat=5), start=1):
    if word[0] not in "01357" and word[-1] not in "26" and word.count("7") <= 2:
        cnt += 1
        # print(number, "".join(word))
print(cnt)