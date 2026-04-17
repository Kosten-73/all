x = 145_682
x2 = 'h' + bin(x)[2:] + 'hhhhhhhhhh'
print(x, x2)
itog2 = ""

def q0(x2, itog2):
    for i in range(len(x2)):
        if x2[i] == 'h':
            itog2 += '1'
            return q1(x2[i + 1:], itog2)

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
            itog2 += '1'
            return itog2
ans2 = q0(x2, itog2).replace('h', '')
print(q0(x2, itog2), ans2)
ans10 = int(ans2, 2)
print(ans10)