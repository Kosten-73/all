from turtle import *

tracer(0)
k = 100
left(90)
right(90)
pendown()
begin_fill()
for i in range(3):
    right(45)
    forward(12 * k)
    right(45)
right(315)
forward(12 * k)
for i in range(2):
    right(90)
    forward(12 * k)
end_fill()
penup()

canvas = getcanvas()
count = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            count += 1
print(count)
done()
