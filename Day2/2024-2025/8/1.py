from itertools import *

cnt = 0
for number, word in enumerate(product(sorted("ИНФОРМАТ"), repeat=5), start=1):
    print(number, "".join(word))
    if number % 2 != 0 and word[0] != "О" and 1 <= word.count("Н") <= 2:
        cnt += 1

print(cnt)
