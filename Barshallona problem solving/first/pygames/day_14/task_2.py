import turtle 
import random
angle = 0
number = int(input())
turtles = []
game_on = True
screen = turtle.Screen()
brush_size = 10
def move_turtles():
    for i in turtles:
        i.forward(5)
def left():
    for i in turtles:
        i.left(20)
def right():
    for i in turtles:
        i.right(20)
def change_color():
    for i in turtles:
        red = random.random()
        blue = random.random()
        green = random.random()
        colors = [red, blue, green] 
        i.color(colors)
def create_a_turtle(num):
    red = random.random()
    blue = random.random()
    green = random.random()
    colors = [red, blue, green]
    t = turtle.Turtle()
    t.color(colors)
    t.speed(0)
    global angle
    t.right(angle)
    angle += 360 / num
    turtles.append(t)
def increase_brush():
    global brush_size
    brush_size += 1
    for i in turtles:
        i.width(brush_size)
def deacrase_brush():
    global brush_size
    brush_size -= 1
    for i in turtles:
        i.width(brush_size)
for i in range(number):
    create_a_turtle(number)
while game_on:
    move_turtles()
    screen.onkey(left, "d")
    screen.onkey(right, "a")
    screen.onkey(change_color, "c")
    screen.onkey(increase_brush,"Up")
    screen.onkey(deacrase_brush,"Down")
    screen.listen()
turtle.done()
