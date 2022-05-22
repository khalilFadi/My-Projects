import turtle 
import random 
#Task 1  and 2
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
colors = ["red", "blue", "green", "yellow"]
def draw_square():
    for i in range(4):
        t.color(colors[i])
        t.forward(50)
        t.left(90)
t.penup()
t.goto(300,300)
t.pendown()
y = 1
c = -1
for i in range(14):
    t.sety(t.ycor() - 50)
    c *= -1
    for x in range(20):
        draw_square()
        t.setx(t.xcor() - (50 * c))
        
    