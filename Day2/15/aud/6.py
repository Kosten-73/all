P = list(range(3, 13 + 1))
Q = list(range(12, 22 + 1))
A = list(range(1, 100))

for x in range(1, 100):
    if not (((x in A) <= (x in P)) or (x in Q)):
        A.remove(x)
print(A)

# 3 = 3
# 22 = 22
# 22 - 3 = 19