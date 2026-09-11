# 1
# for a in range(1001):
#     for x in range(1001):
#         if not (((x & 28 != 0 ) or (x & 45 != 0)) <= ((x & 17 == 0) <= (x & a != 0))):
#             break
#     else:
#         print(a)


# 4

def treyg(n, m, k):
    return (n + m > k) and (n + k > m) and (k + m > n)

def mx(a, b):
    return a if a > b else b

for A in range(1000):
    for x in range(1000):
        # if (treyg(x, 11, 16) == (not(mx(x, 5) > 10))) and treyg(4, A, x):
        if not(not((treyg(x, 11, 16) == (not (mx(x, 5) > 10))) and treyg(4, A, x))):
            break
    else:
        print(A)

print(max(1,4))
print(max(2,1))
print(max(2,1))
print(mx(1,4))
print(mx(2,1))
print(mx(2,1))