def task5_2():
    for n in range(1, 300):
        n2 = bin(n)[2:]
        n2 += str(n2.count("1") % 2)
        print(f"1 Число: {n}, После if: {n2}")
        n2 += str(n2.count("1") % 2)
        print(f"2 Число: {n}, После if: {n2}")
        R = int(n2, 2)
        if R > 123:
            return R
            break
