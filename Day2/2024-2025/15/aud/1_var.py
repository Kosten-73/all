A = list(range(-100, 100))

for x in range(-100, 100):
    if not (((x in A) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in A))):
        A.remove(x)
print(A)
