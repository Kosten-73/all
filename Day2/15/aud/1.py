# A - вакцина
# x - пациенты

for A in range(0, 1000):
    A_ans = True
    for x in range(0, 1000):
        if not((x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))):
            A_ans = False
            break
    if A_ans:
        print(A)
