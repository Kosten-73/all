# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 # if not (x and (not y) or (y == z) or w):
#                     print(x, y, z, w, int(x and (not y) or (y == z) or w))








# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (x or y) and not(y == z) and not w:
#                     print(x, y, z, w)



# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (w<=y) and((x<=z)==(y<=x)):
#                     print(x, y, z, w)

# x y z w
# 0 0 0 0
# 0 0 1 0
# 1 0 1 0
# 1 1 1 0
# 1 1 1 1






# print("x y z w")
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 print(x, y, z, w, int(((x<=y) == (z<= (not w))) and (z or y)))
# x y z w
# 0 0 0 0 0
# 0 0 0 1 0
# 0 0 1 0 1
# 0 0 1 1 0
# 0 1 0 0 1
# 0 1 0 1 1
# 0 1 1 0 1
# 0 1 1 1 0
# 1 0 0 0 0
# 1 0 0 1 0
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 0 0 1
# 1 1 0 1 1
# 1 1 1 0 1
# 1 1 1 1 0


print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                print(x, y, z, w, int(((x<=y) == (z<= (not w))) and (z or y)))













