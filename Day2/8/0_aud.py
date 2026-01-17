from itertools import *

for number, word in enumerate(product(sorted("АБВГДЕЖЗ"), repeat=3), start=1):
    print(number, "".join(word))
    if number == 350:
        print(number, "".join(word))
