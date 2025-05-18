import sys

n = int(input())
s = 0
delta = sys.maxsize
for _ in range(n):
    one, two = map(int, input().split())
    s += min(one, two)
    temp = abs(one - two)
    if (temp < delta) and one % 3 != two % 3:
        delta = temp
if s % 3 == 0:
    s += delta
if delta == sys.maxsize:
    s = 0
print(s)
