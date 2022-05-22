import turtle
t = turtle.Turtle()
t.speed(0)
def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)

def draw_daimond(length):
    for i in range(4):
        t.right(90)
        t.forward(length)

def draw_table(size,length):
    for x in range(size):
        for y in range(size):
            t.setx(x * length)
            t.sety(y * length)
            draw_square(length)
def draw_star(length):
    for i in range(6):
        t.left(144)
        t.forward(length)
draw_star(100)