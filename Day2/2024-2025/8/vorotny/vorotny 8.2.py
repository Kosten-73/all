d = 0
for x1 in '1234567': # тут 0
    for x2 in '01234567':
        for x3 in '01234567':
            for x4 in '01234567':
                for x5 in '01234567':
                    z = x1+x2+x3+x4+x5
                    if z.count('6') == 1:
                        if '16' not in z and '36' not in z and '56' not in z and '76' not in z:  # тут not
                            if '61' not in z and '63' not in z and '65' not in z and '67' not in z:
                                d += 1
print(d)
#код говно
count=0
for x1 in '1234567':
    for x2 in '01234567':
        for x3 in '01234567':
            for x4 in '01234567':
                for x5 in '01234567':
                    s = x1+x2+x3+x4+x5
                    if s.count('6') == 1:
                        if '16' not in s and '36' not in s and '56' not in s and '76' not in s:
                            if '61' not in s and '63' not in s and '65' not in s and '67' not in s:
                                count+=1
print(count)


from itertools import *

cnt1 = 0
cnt2 = 0
for number, word in enumerate(product(sorted("01234567"), repeat=5), start=1):
    # print(number, "".join(word))
    wordStr = "".join(word)
    # 1 способ
    if word[0] != "0" and word.count("6") == 1 and \
            "16" not in wordStr and "61" not in wordStr and \
            "36" not in wordStr and "63" not in wordStr and \
            "56" not in wordStr and "65" not in wordStr and \
            "76" not in wordStr and "67" not in wordStr:
        cnt1 += 1
    # 2 способ
    if word[0] != "0" and word.count("6") == 1 and \
            all(f"{d}6" not in wordStr and f"6{d}" not in wordStr for d in "1357"):
        cnt2 += 1

print(cnt1)
print(cnt2)

print(000001)