# картинка "задача 5 из егэ 1"
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


# картинка "задача 5 из егэ 2"
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

        # print(f"Число: {n}, После if: {n2}, d = {d}")

        # print(f"Число: {n}, После if: {n2}")

        # % - остаток от деления
        # // - целочисленное деление




# картинка "задача 5 из егэ 3"

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






print(task5_3())

print(True)
print(int(True))
print(int(False))
#now = "123456789"
