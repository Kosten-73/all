def task5_3():
    for n in range(1, 1000):
        n2 = bin(n)[2:]
        n2 += n2[-1]
        # Не оптимизированный код
        # n3 = n2 + n2[-1]
        # if n2.count("1") % 2 == 0:
        #     n3 += "0"
        # else:
        #     n3 += "1"
        # if n3.count("1") % 2 == 0:
        #     n3 += "1"
        # else:
        #     n3 += "0"

        n2 += str(bin(n)[2:].count("1") % 2)
        n2 + str(1 - n2.count("1") % 2)
        N = int(n2, 2)
        if N > 553:
            return N