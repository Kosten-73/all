from math import sqrt


def is_prime(x):
    for now in range(2, int(sqrt(x))):
        if x % now == 0:
            return False
    return True


for n in range(1, 1_000):
    s = ">" + "0" * 21 + "1" * n + "2" * 13
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    suma = s.count('1') + s.count('2') * 2
    if is_prime(suma):
        print(suma, n)
        break
