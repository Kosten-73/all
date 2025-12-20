from turtle import*
left(90)
k = 15
speed(5)
down()
for i in range(7):
    forward(10*k)
    right(120)
up()
for x in range(-10,20):
    for y in range(-10,20):
        goto(x*k,y*k)
        dot()
done()
    
