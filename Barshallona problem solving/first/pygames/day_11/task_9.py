#draw shape according to angles 
import turtle
t = turtle.Turtle()
t.speed(0)
def draw_shape(length, num_sides):
    sides = 360 / num_sides
    for i in range(num_sides):
        t.forward(length)
        t.right(sides)
draw_shape(100, 5)