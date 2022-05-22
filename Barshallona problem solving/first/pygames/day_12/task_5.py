import turtle
import task_2
import random
t = turtle.Turtle()
cordinates = [0, 0]
positions = [cordinates]
def nearest_two(num):
    if num % 2 == 0:
        return num
    else:
        return num + 1
class spawn_fruit():
    def __init__(self):
        t.color("green")
        x = random.randint(-240,240)
        y = random.randint(-240,240)
        positions.append([x, y])
        original_color = t.color
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(-0.5)
        t.forward(1)
        t.color = original_color

screen  = turtle.Screen()
gameover = True
t.penup()
t.speed(0)
t.goto(-250,250)
t.pendown()
t.color("red")
t.width(10)
for i in range(4):
    t.forward(500)
    t.right(90)
for i in range(20):
    spawn_fruit()
t.penup()
t.color("blue")
t.goto(0,0)
t.pendown()
t.speed(10)

while gameover:
    t = task_2.turtle_movement(t, screen)
    t.goto(int(t.xcor()), int(t.ycor()))
    t.forward(4)
    print(positions.__len__() - 1)
    for i in range(positions.__len__() - 1):
        if int(positions[i][0]) == int(t.xcor()) and int(positions[i][1]) == int(t.ycor()):
            t.write("goodjob")
    if t.xcor() < -250 or t.xcor() > 250 or t.ycor() < -250 or t.ycor() > 250:
        t.write("game over")
        gameover = False
turtle.done()

