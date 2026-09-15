print("x y z w F1 F2")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F1 = (x == y) and (w <= z)
                F2 = (x <= y) <= (z == w)
                print(x, y, z, w, int(F1), '', int(F2))
# x y z w F1 F2
# 0 0 0 0 1  1
# 0 0 0 1 0  0
# 0 0 1 0 1  0
# 0 0 1 1 1  1
# 0 1 0 0 0  1
# 0 1 0 1 0  0
# 0 1 1 0 0  0
# 0 1 1 1 0  1
# 1 0 0 0 0  1
# 1 0 0 1 0  1
# 1 0 1 0 0  1
# 1 0 1 1 0  1
# 1 1 0 0 1  1
# 1 1 0 1 0  0
# 1 1 1 0 1  0
# 1 1 1 1 1  1




# x y z w F1 F2
# 1 1 1 0 1  0
# 0 1 1 0 0  0
# 0 0 1 1 1  1
