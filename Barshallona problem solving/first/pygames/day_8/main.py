import turtle 
import random
t = turtle.Turtle()
t.speed(0)
#this didnt work for some reason 
# red = random.randint(0,200)
# blue = random.randint(0,200)
# green = random.randint(0,200)
def draw_square(length, color):
    i = 1
    t.fillcolor(color)
    t.begin_fill()
    while (i < 5): 
        t.right(90)
        t.forward(length)
        i += 1
    t.end_fill()
colors = ["red", "blue", "green", "yellow", "pink", "black"]
for i in range(40):
    # color = (red, blue, green)
    
    t.right(10)
    for i in range(50):
        num = random.randint(0,5)
        t.color(colors[num])
        t.right(10)
        length = random.randint(20, 200)
        draw_square(length, colors[num])
    # t.circle(50)