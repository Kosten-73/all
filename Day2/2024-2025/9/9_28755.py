f=open("9_28755.txt")
k=0
for s in f :
    a=sorted([int(x) for x in s.split()])
    #if max(a)<sum(a)-max(a):
    if a[-1]<sum(a[:-1]):
        #if a[0]+a[1]!= a[2]+a[3] and a[0]+a[2]!=a[1]+a[3] and a[0]+a[3]!=a[1]+a[2]:

        if a[0]+a[3]!=a[1]+a[2]:
            k+=1
print(k)