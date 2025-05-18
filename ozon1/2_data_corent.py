def vicoko(got):
    return (got % 4 == 0 and got % 100 != 0) or got % 400 == 0


def osnova(n):
    for i in range(n):
        day, month, year = list(map(int, input().split()))
        if 1 <= day <= 31 and 1950 <= year <= 2300 and 1 <= month <= 12:
            if month in [1, 3, 5, 7, 8, 10, 12]:
                print('YES')
            if month in [4, 6, 9, 11]:
                if day <= 30:
                    print('YES')
                else:
                    print('NO')
            if month == 2:
                if vicoko(year):
                    if day <= 29:
                        print('YES')
                    else:
                        print('NO')
                elif day <= 28:
                    print('YES')
                else:
                    print('NO')
        else:
            print('NO')


osnova(int(input()))
