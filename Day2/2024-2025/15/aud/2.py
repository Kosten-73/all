def DEL(n, m):
    return n % m == 0


for A in range(1, 10000):
    for x in range(1, 10000):
        if not ((not (DEL(x, A))) <= (DEL(x, 6) <= (not (DEL(x, 9))))):
            break
    else:
        print(A)
