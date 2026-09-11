def f(x):
    return (((5 <= x <= 30) == (14 <= x <= 23)) <= (not (a <= x <= b)))

r = [ ]
d = [y for x in(5,14,23,30) for y in (x,x + 0.1 , x - 0.1)]
for a in d:
    for b in d:
        if b >= a and all(f(x) == 1 for x in d):
            r += [b - a]
print(max(r))
print(int(False))