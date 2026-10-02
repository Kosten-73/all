def task5_1():
    for n in range(1, 300):
        n2 = bin(n)[2:]
        if n % 2 == 0:
            n2 += "10"
        else:
            n2 += "01"
        d = int(n2, 2)
        if d > 200:
            return d
            # print(f"Число: {n}, После if: {n2}, d = {d}")

        # print(f"Число: {n}, После if: {n2}")

        # % - остаток от деления
        # // - целочисленное деление
