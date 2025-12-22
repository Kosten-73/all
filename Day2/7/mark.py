# def t_sec(b, s, d, v):
#     return v / (s * b * d)

b = 64000
s = 2
d = 24
v = 220 * 2**23

t = v / (s * b * d)

print(int(t / 60))

# print(int(t_sec(b, s, d, v) / 60))
