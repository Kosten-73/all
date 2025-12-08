from turtle import *
m = 20 # Масштаб
tracer(0)
screensize(5000, 5000) # увеличим размер окна
pd() # опускаем хвост
left(90) # поворачиваем голову в сторону
# положительного направления оси ординат
# Алгоритм
for i in range(2):
	forward(14 * m)
	right(90)
	forward(18 * m)
	right(90)
pu() # поднимаем хвост
forward(3 * m)
right(90)
forward(7 * m)
left(90)
pd() # опускаем хвост
for i in range(2):
	forward(74 * m)
	right(90)
	forward(92 * m)
	right(90)
pu()# поднимаем хвост
    # Проставление точек
for x in range(-10, 100):
	for y in range(-10, 110):
		goto(x * m, y * m)
		dot(3)
done()