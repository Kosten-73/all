def cc_10_in_5(elem, osnova):
    str_i = ''
    while elem > 0:
        str_i += str(elem % osnova)
        elem //= osnova
    return str_i[::-1] == str_i
def prostoe(elem):
    flag = True
    for i in range(2, int(elem**0.5) + 1):
        if elem % i == 0:
            flag = False
            break
    return flag

k = 0
osnova = 5
for i in range(2, 1000000):
    if prostoe(i):
        if cc_10_in_5(i, osnova):
            k += 1
print(k)
#
# 152