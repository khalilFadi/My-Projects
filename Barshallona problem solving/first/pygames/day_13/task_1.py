import turtle
import random
t = turtle.Turtle()
screen = turtle.Screen()
r = 8
def draw_square(x, y):
    global r
    if r != 0:
        angle = 360 / r
    for i in range(r):
        t.forward(100)
        t.right(angle)
    if r <= 0:
        t.right(180)
        r = 8
    r -= 1
screen.onclick(draw_square)
screen.listen()
turtle.done()