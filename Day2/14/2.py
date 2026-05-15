from main import perevodCC

# print(perevodCC(52, 3))
# print(52 == int("1221", 3))

s = 9**8 + 3**24 - 3*7
cnt2 = 0
while s > 0:
    if s % 3 == 2:
        cnt2 += 1
    s //= 3
print(cnt2)

s1 = 9**8 + 3**24 - 3*7
digits = []
while s1 > 0:
    digits.append(s1 % 3)
    s1 //= 3
print(digits.count(2))