# A - вакцина
# x - пациенты

for A in range(0, 1000):
    flag_a = True
    flgA = True
    znachenie_A = True
    for x in range(0, 1000):
        if ((x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))) == False:
            flag_a = False
            break
    if flag_a:
        print(A)
        break

for A in range(0, 1000):
    for x in range(0, 1000):
        if ((x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))) == False:
            break
    else:
        print(A)
        break