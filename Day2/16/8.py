def F(n):
    if n == 0:
        return 5
    if n > 0 and n % 2 == 0:
        return 1 + F(n - 2)
    if n > 0 and n % 2 != 0:
        return F(n // 2)

count = 0
for i in range(1, 1001):
    if F(i) == 7:
        count += 1
print(count)


# print(*range(1, 5))
a = [1, 4, 5]
# print(a)
# print(*a)
# print(','.join(a))
