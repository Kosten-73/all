print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not y or x) and w and not z:
                    print(x, y, z, w)
# x y z w
# 0 0 0 1
# 1 0 0 1
# 1 1 0 1