n = int(input("Введите n = "))
s = 0
k = 0
for i in range(n):
    t = int(input())
    if len(str(abs(t))) == 3:
        s += t
        k += 1
print("среднее арифметическое = ", s / k)
