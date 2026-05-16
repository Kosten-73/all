from string import *

alph = digits + ascii_uppercase
print(alph[18::-1])
for x in alph[18::-1]:
    s = (int(f"98{x}79641", 19) +
         int(f"36{x}14", 19) +
         int(f"73{x}4", 19))
    if s % 18 == 0:
        print(x, s // 19)
