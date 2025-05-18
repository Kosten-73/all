def cc_10_in_7_and_palindrom(elem_10):
    stri = ''
    while elem_10 > 0:
        stri += str(elem_10 % 7)
        elem_10 //= 7
    return stri == stri[::-1]
def proverka_prostotu(elem):
    if elem == 0 or elem == 1:
        return
    if elem == 2 or elem == 3:
        return elem
    for i in range(2, int(elem**0.5) + 1):
        if elem % i == 0:
            return
    return elem

k = 0
for now in range(1000000):
    p = proverka_prostotu(now)
    if p != None:
        if cc_10_in_7_and_palindrom(p):
            k += 1
print(k)


