import random 
import turtle
t = turtle.Turtle()
t.speed(0)
for i in range(120):
    t.right(3)
    r = random.randint(50,100)
    for x in range(4):
        t.forward(r)
        t.right(90)
