def count_color(count_bit):
    return 2**count_bit


N = 128 * 320
V = 40 * 2**13

# i = V / N

# print((128 * 320) / (40 * 2**13))
print(2**((40 * 2**13) / (128 * 320) ))