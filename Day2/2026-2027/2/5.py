print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) == (z <= (not w)) and (z or y))
                print(x, y, z, w, int(F))


# 0 1 1 1 0
# 0 0 1 0 1
# 0 1 0 0 1
# 0 1 0 1 1
# 0 1 1 0 1
# 1 1 0 0 1
