# тёртл
from turtle import *

tracer(0)
KEF = 100
# опустить хвост
pendown()
# Потому что ось ординат
left(90)
begin_fill()
for i in range(4):
    forward(123 * KEF)
    right(120)
end_fill()
penup()
# for x in range(-300, 300):
#     for y in range(-300, 300):
#         setpos(x * KEF, y * KEF)
#         dot(2, "red")
canvas = getcanvas()
count = 0
for x in range(-300, 300):
    for y in range(-300, 300):
        # setpos(x * KEF, y * KEF)
        # dot(4, "red")
        # print(canvas.find_overlapping(x * KEF, y * KEF, x * KEF, y * KEF))
        if canvas.find_overlapping(x * KEF, y * KEF, x * KEF, y * KEF) == (5,):
            count += 1
print(count)
done()
