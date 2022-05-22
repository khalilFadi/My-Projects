import random 
import turtle
t = turtle.Turtle()
length = 10
t.width(3)
t.speed(0)
t.shape("turtle")
increase = 10
colors = ["red", "green", "blue", "orange", "black", "cyan", "orange", "pink"]
for i in range(50):
    n = random.randint(0,7)
    t.color(colors[n])
    t.forward(length)
    length += increase
    increase += 0.5
    t.right(90)