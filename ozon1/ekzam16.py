def cc_10_in_6(elem):
    stri = ''
    while(elem > 0):
        stri += str(elem % 6)
        elem //= 6
    return stri[::-1] == stri
def prostoe(elem):
    flag = True
    for i in range(2, int(elem**0.5) + 1):
        if elem % i == 0:
            flag = False
    return flag


k = 0
for i in range(2, 1000000):
    if prostoe(i):
        if cc_10_in_6(i):
            k += 1
print(k)
