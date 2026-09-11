# тёртл
from turtle import *
tracer(0)

KEF = 1000
# опустить хвост
pendown()

begin_fill()
for i in range(6):
    forward(3 * KEF)
    left(60)
end_fill()
penup()

# for x in range(-10, 10):
#     for y in range(-10, 10):
#         setpos(x * KEF, y * KEF)
#         dot(4, "white")

canvas = getcanvas()
count = 0
for x in range(-50, 50):
    for y in range(-50, 50):
        # setpos(x * KEF, y * KEF)
        # dot(4, "red")
        # print(canvas.find_overlapping(x * KEF, y * KEF, x * KEF, y * KEF))
        if canvas.find_overlapping(x * KEF, y * KEF, x * KEF, y * KEF) != ():
            count += 1
print(count)

done()