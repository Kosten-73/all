from turtle import *

tracer(0)
KEF = 10

pendown()
left(90)
right(90)
begin_fill()
for _ in range(3):
    right(45)
    forward(12 * KEF)
    right(45)
right(315)
forward(12 * KEF)
for _ in range(2):
    right(90)
    forward(12 * KEF)
penup()
end_fill()


canvas = getcanvas()

count = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if canvas.find_overlapping(x * KEF, y * KEF, x * KEF, y * KEF) != ():
            count += 1
print(count)
done()