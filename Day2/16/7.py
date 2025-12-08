def F(n):
    if n >= 2025:
        return n
    # if n < 2025:
    return n + F(n + 2)


print(F(2020) - F(2023))


# print(*range(1, 5))
a = [1, 4, 5]
# print(a)
# print(*a)
# print(','.join(a))
