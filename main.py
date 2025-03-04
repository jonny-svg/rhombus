import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("yellow")

t = turtle.Turtle()

t.setheading(135)
t.fillcolor("cyan")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

turtle.done()