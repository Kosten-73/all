from turtle import *

tracer(0)
k = 100
left(90)
pendown()
begin_fill()
for i in range(2):
    right(90)
    forward(120 * k)
    right(90)
    forward(14 * k)
end_fill()
penup()


count = 0
canvas = getcanvas()
for x in range(-500, 500):
    for y in range(-500, 500):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
            count += 1
print(count)
done()
