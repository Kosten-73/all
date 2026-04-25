from itertools import*
alf="ГЕРАСИМ"
k=0
for x in product(alf, repeat = 7 ):
    s = ''.join(x)
    if len(set(s))==7:
        s=(s.replace("Г","0").replace("Р","0")
           .replace("С","0").replace("М","0")
           .replace("А","1").replace("Е","1").replace("И","1"))
        if "11" not in s  and "00" not in s:
            k+=1
print(k)

