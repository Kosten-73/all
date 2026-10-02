def task5_4():
    for n in range(1, 300):
        n2 = bin(n)[2:]
        if n % 2 != 0:
            n2 += "0"
        else:
            n2 = "1" + n2
        print(f"1 Число: {n}, После if: {n2}")
        if n2.count("1") % 2 == 0:
            n2 += "1"
        else:
            n2 += "0"
        print(f"2 Число: {n}, После if: {n2}")
        R = int(n2, 2)
        if R > 300:
            return R
print(task5_4())
