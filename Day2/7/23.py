k = 2
f = 48000
b = 34
t = 42 * 60 + 20
speed = 314572800
Vzag = 110 * 2**13
count = 13

print((2 * f * b * t + count * Vzag) / speed)