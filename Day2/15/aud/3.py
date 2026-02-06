# for A in range(1, 1000):
#     a_ans = True
#     for x in range(0, 1000):
#         for y in range(0, 1000):
#             if not((2 * x + y != 70) or (x < y) or (A < x)):
#                 a_ans = False
#                 break
#         if not a_ans:
#             break
#     if a_ans:
#         print(A)

for A in range(1, 1000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((2 * x + y != 70) or (x < y) or (A < x)):
                break
        if not ((2 * x + y != 70) or (x < y) or (A < x)):
            break
    else:
        print(A)
