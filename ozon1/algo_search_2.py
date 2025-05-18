def poisk(mas, elem):
    l = 0
    r = len(mas) - 1
    while l <= r:
        m = l + int((r - l) / 2)
        if elem == mas[m]:
            return m, mas[m]
        elif elem > mas[m]:
            l = m + 1
        else:
            r = m - 1
    return -1

arr = [-3, 0, 1, 1, 12, 13, 31, 32, 93, 100]
print(poisk(arr, 33))
