from turtle import *
from random import *
s = Screen()


#Square
square = Turtle()
square.shape("square")
square.color("red")
square.shapesize(3)
square.penup()
square.setx(200)

#Circle
circle = Turtle()
circle.penup()
circle.color("blue")
circle.shapesize(3)
circle.shape("circle")
circle.setx(-100)
circle.right(45)
C_width = 20

#mouse
mouse = Turtle()
mouse.penup()
mouse.shapesize(3)
mouse.setheading(90)
mouse.sety(-200)

num = 0
direction = -10
def Square_movment():
    global direction
    global num
    if num > 60:
        num = 0
        direction *= -1
    num += 1
    square.forward(direction)

angle = 10
def circle_movment():
    global angle
    num = randrange(10, 90)
    negat = randrange(-1, 1)
    if circle.xcor() + C_width >= s.canvwidth or circle.xcor() - C_width <= -s.canvwidth:        
        circle.right(90)
    if circle.ycor() + C_width >= s.canvheight or circle.ycor() - C_width <= -s.canvheight:
        circle.right(90)
    circle.forward(angle)

num2 = 0
direction2 = 10
def mouse_move():
    global direction2
    global num2
    if num2 > 60:
        num2 = 0
        direction2 *= -1
    num2 += 1
    mouse.forward(direction2)

def Start_square(x, y):
    for i in range(120):
        circle_movment()
        Square_movment()
        mouse_move()

def main():
    circle_movment()
    s.onclick(Start_square)

running = True
while(running):
    main()
