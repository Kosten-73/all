def test_task(stri):
    flag = True
    if stri[0] == 'M':
        if stri[-1] == 'D':
            for i in range(1, len(stri) - 1):
                if stri[i] == 'M':
                    if stri[i + 1] == 'M':
                        flag = False
                if stri[i] == 'R':
                    if stri[i + 1] != 'C':
                        flag = False
                if stri[i] == 'C':
                    if stri[i + 1] != 'M':
                        flag = False
                if stri[i] == 'D':
                    if stri[i + 1] != 'M':
                        flag = False
        else:
            flag = False
    else:
        flag = False
    if flag:
        print('YES')
    else:
        print('NO')


for _ in range(int(input())):
    test_task(input())
