import task_9
import turtle 
import random
t = turtle.Turtle()
screen = turtle.Screen()
t.color("blue")
def go_to_position(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    r = random.random()
    b = random.random()
    g = random.random()
    colors = [r,b,g]
    t.fillcolor(colors)
    t.color(colors)
    t.begin_fill()
    length = random.randint(50,150)
    angles = random.randint(3,6)
    task_9.draw_shape(length, angles, t)
    t.end_fill()
screen.onclick(go_to_position)
screen.listen()
turtle.done()