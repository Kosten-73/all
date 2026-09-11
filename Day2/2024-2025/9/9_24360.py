f = open('9_24360.txt')
k=0
mins = 10**10
for s in f:
    a = [int(x) for x in s.split()]
    a.sort()
    pov = 0
    fl1 = True
    if min(a)**2 in a:
        mins= min(mins, sum(a))
        fl1 = False
    for i in set(a):
        pov += a.count(i)//2
    if pov >= 3:
        if fl1:
            mins = min(mins, sum(a))
if mins != 10**10:
    print(mins)
