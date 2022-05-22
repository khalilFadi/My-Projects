import turtle 
import random 
t = turtle.Turtle()
t.speed(0)
t.penup()
t.setx(-300)
t.sety(-300)
t.pendown()
for i in range(30):
    n = random.randint(10,40)
    k = random.randint(20,50)
    t.forward(k)
    t.left(90)
    t.forward(n)
    t.right(90)