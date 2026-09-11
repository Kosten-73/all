def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1 and n % 2 == 0:
        return 2 + int(3 * F(n - 1) / 3)
    if n > 1 and n % 2 != 0:
        return 2 * n + int((F(n - 1) + F(n - 3) + 2) / 3)

# n % 2 != 0 and n
print(-5 % 2 != 0)
print(-7 % 2 == 1)
print(F(30))

print(5.6)
print(int(5.6))
print(round(4.9))