from itertools import *

i = 1
for word in product("АБВГДЕЖЗ", repeat=3):
    if i == 350:
        print(i, word)
    i += 1


# for number, word in enumerate(permutations(sorted("ААБВГДЕЖЗ"), r=3), start=1):
#     print(number, "".join(word))

# for number, word in enumerate(permutations(set(sorted("ММАРИНА")), r=3), start=1):
#     print(number, "".join(word))

# permutations