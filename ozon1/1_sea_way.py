def count_data(t):
    for i in range(t):
        temp = input()
        count_1, count_2, count_3, count_4 = 0, 0, 0, 0
        for now in temp.split():
            if now == '1':
                count_1 += 1
            elif now == '2':
                count_2 += 1
            elif now == '3':
                count_3 += 1
            elif now == '4':
                count_4 += 1
        if count_1 == 4 and count_2 == 3 and count_3 == 2 and count_4 == 1:
            print("YES")
        else:
            print("NO")


count_data(int(input()))
