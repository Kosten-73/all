# print(bin(52)[2:]) # в 2 сс
# print(oct(52)[2:]) # в 8 сс
# print(hex(52)[2:]) # в 16 сс
# print(int("10110", 2))
# print(int("AA", 16))
# print(int("AA", 36))













def perevodCC(x, cc):
    out = ""
    while x > 0:
        out += str(x % cc) # out = str(x % cc) + out
        x //= cc
    return out[::-1] # return out