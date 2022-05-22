#random squares 
import random 
import turtle
t = turtle.Turtle()
t.speed(0)
def draw_square():
    t.penup()
    r = random.random()
    b = random.random()
    g = random.random()
    color = (r, g, b)
    t.color(color)
    r = random.randint(-400,400)
    t.setx(r)
    r = random.randint(-400,400)
    t.sety(r)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    r = random.randint(50,200)
    for i in range(4):
        t.forward(r)
        t.right(90)
    t.end_fill()
for i in range(50):
    draw_square()