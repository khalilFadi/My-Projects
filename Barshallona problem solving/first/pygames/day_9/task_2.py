import random 
import turtle
b = turtle.Turtle()
b.color("blue")
b.shape("turtle")
b.penup()
b.setx(-250)
b.sety(90)
b.pendown()
e = turtle.Turtle()
e.color("red")
e.penup()
e.setx(-250)
e.sety(70)
e.pendown()
e.shape("turtle")
f = turtle.Turtle()
f.penup()
f.setx(-250)
f.sety(50)
f.pendown()
f.color("green")
f.shape("turtle")
for i in range(25):
    ran = random.randint(5,20)
    b.forward(ran)
    ran = random.randint(5,20)
    e.forward(ran)
    ran = random.randint(5,20)
    f.forward(ran)
if b.xcor() > e.xcor():
    if b.xcor() > f.xcor():
        b.write("u all r losers", font=("lemon", 20, "normal"))
    elif f.xcor() > b.xcor():
        f.write("u all r losers", font=("lemon", 20, "normal"))
    else :
        e.write("u all r losers", font=("lemon", 30, "normal"))