def task14():
    s = 0
    razXY = 20001
    for i in range(int(input())):
        x, y = map(int, input().split())
        if x>y:
            m = y
        else:
            m = x
        s += m
        if abs(x-y) < razXY and x % 4 != y % 4:
            razXY = abs(x-y)
    if s % 4 == 0 and razXY != 20001:
        s += razXY
    if razXY == 20001:
        s = 0
    return s

print(task14())

