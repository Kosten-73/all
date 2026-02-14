a = int(input())
k = 0
while a != 0:
    if a > 0 and a % 5 == 0:
        k += 1
    a = int(input())
print(k)
