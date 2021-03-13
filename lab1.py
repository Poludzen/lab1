import turtle

turtle.bgcolor("black")
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
t = turtle.Pen()
t.speed(10)
for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

t.width(1)
for i in range(180):
    t.pencolor(colors[i % 6])
    t.forward(100)
    t.right(30)
    t.forward(20)
    t.left(60)
    t.forward(50)
    t.right(30)
    t.penup()
    t.setposition(0, 0)
    t.pendown()
    t.right(2)

turtle.done()