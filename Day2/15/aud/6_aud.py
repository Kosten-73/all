P = list(range(3, 14))
Q = list(range(12, 22))

for A in range(1, 1000):
    for x in range(1, 100):
        if not (((x in A) <= (x in P)) or (x in Q)):
            break
    else:
        print(A)
