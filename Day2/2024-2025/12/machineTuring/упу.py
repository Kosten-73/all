x = 2028
x2 = bin(x)[2:] + 'hhhhh'
print(x, x2)
itog2 = ""

def q1(x2, itog2):
    for i in range(len(x2)):
        if x2[i] == '0':
            itog2 += '0'
        if x2[i] == '1':
            itog2 += '1'
        if x2[i] == 'h':
            itog2 += '0'
            return q2(x2[i + 1:], itog2)

def q2(x2, itog2):
    for i in range(len(x2)):
        if x2[i] == 'h':
            itog2 += '0'
            return q3(x2[i + 1:], itog2)

def q3(x2, itog2):
    for i in range(len(x2)):
        if x2[i] == 'h':
            itog2 += 'h'
            return itog2
ans2 = q1(x2, itog2).replace('h', '')
print(ans2)
ans10 = int(ans2, 2)
print(ans10)