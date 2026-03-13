def f(n, m):
    return n % m == 0


for A in range(1, 1000):
    for x in range(1, 1000):
        if not (((f(x, 2)) <= (not (f(x, 3)))) or ((x + A) >= 100)):
            break
    else:
        print(A)
