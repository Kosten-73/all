s = 3 * 289**2024 + 81 * 49**121 - 9 * 16**81 - 6011
summa17 = 0
while s > 0:
    if s % 31 <= 17:
        summa17 += s % 31
    s //= 31
print(summa17)
