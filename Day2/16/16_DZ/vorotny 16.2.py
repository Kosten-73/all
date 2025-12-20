from sys import setrecursionlimit
setrecursionlimit(10000)
def f(n):
    if n == 1:
        return n
    if n > 1:
        return n-1 + f(n-1)
print(f(2024) - f(2022))
