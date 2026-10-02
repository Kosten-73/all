def task5_5(mas):
    for n in range(1, 300):
        n2 = bin(n)[2:]
        if n % 2 == 0:
            n2 = "1" + n2 + "10"
        else:
            n2 = "11" + n2 + "0"
        R = int(n2, 2)
        if R > 130:
            mas.append(R)
    return mas
mas = []
print(min(task5_5(mas)))