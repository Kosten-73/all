

def way_rob():
    global i_pos, j_pos
    mas = list()
    n, m = list(map(int, input().split()))
    elem = ''
    for i in range(n):
        mas.append(list(input()))
        for j in range(len(mas[i])):
            if mas[i][j] == 'A' and elem == '':
                elem = 'A'
                pos_i, pos_j = i, j
            if mas[i][j] == 'B' and elem == '':
                elem = 'B'
                pos_i, pos_j = i, j
            if elem != '' and mas[i][j] != elem and mas[i][j] != '#' and mas[i][j] != '.':
                elem_anti = mas[i][j]
                i_pos, j_pos = i, j

    while mas[0][0] == '.':
        if pos_i > 0 and mas[pos_i - 1][pos_j] == '.':
            pos_i -= 1
            mas[pos_i][pos_j] = elem.lower()
            continue
        if mas[pos_i][pos_j - 1] == '.' and pos_j > 0:
            pos_j -= 1
            mas[pos_i][pos_j] = elem.lower()
            continue

        if pos_j < m and mas[pos_i][pos_j + 1] == '.':
            pos_j += 1
            mas[pos_i][pos_j] = elem.lower()
            continue

        if pos_i < n and mas[pos_i + 1][pos_j] == '.':
            pos_i += 1
            mas[pos_i][pos_j] = elem.lower()
            continue


    while mas[n - 1][m - 1] == '.':
        if i_pos < n - 1 and mas[i_pos + 1][j_pos] == '.':
            i_pos += 1
            mas[i_pos][j_pos] = elem_anti.lower()
            continue

        if j_pos < m - 1 and mas[i_pos][j_pos + 1] == '.':
            j_pos += 1
            mas[i_pos][j_pos] = elem_anti.lower()
            continue

        if j_pos > 0 and mas[i_pos][j_pos - 1] == '.':
            j_pos -= 1
            mas[i_pos][j_pos] = elem_anti.lower()
            continue

        if i_pos > 0 and mas[i_pos - 1][j_pos] == '.':
            i_pos -= 1
            mas[i_pos][j_pos] = elem_anti.lower()
            continue




    for now in mas:
        for won in now:
            print(won, end='')
        print()

for _ in range(int(input())):
    way_rob()
