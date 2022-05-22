#square fan 
import turtle
import random
t = turtle.Turtle()
t.speed(0)
def draw_shape(length, num_sides):
    sides = 360 / num_sides
    for i in range(num_sides):
        t.forward(length)
        t.right(sides)
def draw_increase_squares():
    for x in range(4):
        length = 40
        for i in range(10):
         length +=10
         draw_shape(length, 4)
        t.right(90)
draw_increase_squares()

