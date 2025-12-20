def t_sec(b, s, d, v):
    return v / (s * b * d)


b = 64000
s = 2
d = 24
v = 220 * 2**23

print(int(t_sec(b, s, d, v) / 60))
