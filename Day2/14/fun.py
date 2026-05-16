def F(x, n):
    out = ""
    while x > 0:
        out += str(x % n)
        x //= n
    return out[::-1]

# print(F(10, 2))
# print(F(123123, 8))