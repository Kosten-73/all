n = int(input("Введите n = "))
s = 0
k = 0
for i in range(n):
    t = int(input())
    if len(str(abs(t))) == 2:
        s += t
        k += 1
print("сумма = ", s)
print("количество = ", k)
print("среднее арифметическое = ", s / k)
