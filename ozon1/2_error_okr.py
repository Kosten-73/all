for i in range(int(input())):
    stri = list(map(int, input().split()))
    s = 0
    for j in range(stri[0]):
        x = int(input()) * stri[1] / 100
        s += x - int(x)
    print('{:.2f}'.format(s))
