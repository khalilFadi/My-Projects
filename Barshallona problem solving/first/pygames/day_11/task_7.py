#square loop or the circle thi
import turtle
t = turtle.Turtle()
t.speed(0)
def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)
for i in range(120):
    t.right(3)
    draw_square(100)