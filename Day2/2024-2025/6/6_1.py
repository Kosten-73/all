# тёртл
from turtle import *
# print(help())
# быстрая отрисовка
tracer(0)
# опустить хвост
pendown()
k = 30
# заливка
begin_fill()
for i in range(6): # 24
    forward(3 * k)
    left(60)
end_fill()
# убрать хвост
penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * k, y * k)
        dot(5)

# canvas = getcanvas()
# count = 0
# for x in range(-15, 15):
#     for y in range(-15, 15):
#         if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
#             count += 1
# print(count)
done()
