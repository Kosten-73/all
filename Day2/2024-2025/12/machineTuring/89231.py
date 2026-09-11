otv = []
for i in range(10**6):
    s = bin(i)[2:]
    s = s.replace('0','1')
    s = '110' + s + '1'
    s = int(s,2)
    if s < 941:
        otv.append(s)
print(max(otv))