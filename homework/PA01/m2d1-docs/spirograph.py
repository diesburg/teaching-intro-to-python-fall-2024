import turtle,time

t = turtle.Pen()
t.penup() #Not required with Python
t.goto(0,0) #Not required with Python
t.setheading(0) #Not required with Python
t.speed(10) #No equivalent in Scratch
time.sleep(1)
t.pendown()
for outerLoop in range(20):
    for innerLoop in range(4):
        t.forward(100)
        t.right(90)
    t.right(18)
t.penup()
t.goto(180,-120)
