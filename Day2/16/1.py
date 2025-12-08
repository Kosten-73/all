def F(n):
    if n < 2:
        return 1
    # if n >= 2:
    return F(n - 1) * (n + 5)

print(F(5))
