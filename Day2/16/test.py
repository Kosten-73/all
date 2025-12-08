def f(n):
    if n <= 1:
        return 1
    return  n * f(n - 1)

def f1(n):
    if n < 2:
        return 1
    return (n + 5) * f1(n - 1)













def f2(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return f2(n / 2)
    if n > 0 and n % 2 != 0:
        return 1 + f2(n - 1)

def G(n):
    if n == 1:
        return 1
    if n > 1:
        return f3(n - 1) + 5 * n
def f3(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * G(n) + 3 * n



print(f1(5))
print(f2(12))
print(f3(4) - G(5))