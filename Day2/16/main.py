a = 5
b = 6
c = -5
def my_max(a, b):
    print(c)
    if a > b:
        return a
    else:
        return b

b = 7
a = -2

# if a > b:
#     print(a)
# else:
#     print(b)

print(my_max(5, 7))
print(my_max(-4, 4))
print(my_max(-3, 6))
print(my_max(4, 4))


def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)
print(f(5))
# 5 = 5 * 4 * 3 * 2 * 1