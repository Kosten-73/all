from math import sqrt
from turtle import *

tracer(0)
k = 100
left(90)
right(60)
pendown()
begin_fill()
for i in range(2):
    forward(10 * k)
    right(120)
    forward(5 * k)
    right(240)
right(120)
forward(3 * k)
right(90)
forward(k * sqrt(1200))
right(90)
forward(8 * k)
right(120)
for i in range(2):
    forward(10 * k)
    left(120)
    forward(5 * k)
    left(240)
end_fill()
penup()


count = 0
canvas = getcanvas()
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            count += 1
print(count)
done()
