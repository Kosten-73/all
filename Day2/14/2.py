def perevodCC(x, cc):
    out = ""
    while x > 0:
        out += str(x % cc) # out = str(x % cc) + out
        x //= cc
    return out[::-1] # return out

print(perevodCC(52, 3))
print(52 == int("1221", 3))