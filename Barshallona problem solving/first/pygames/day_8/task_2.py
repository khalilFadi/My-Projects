import turtle
import random 
t = turtle.Turtle()
ran = random.randint(100,200)
side = 1
while (side <= 4):
     t.forward(ran)
     t.right(90)
     side += 1
      