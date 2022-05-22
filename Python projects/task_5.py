import turtle

t = turtle.Turtle()
t.penup()
t.goto(0,-200)
t.pendown()
t.setheading(90)
t.color("brown")
def draw_branch(t1, lan, num):
    if num > 7:
        return 1
    t1.forward(lan)
    angle = 20
    t2 = t1.clone()
    t2.left(20)
    t1.right(20)
    draw_branch(t2, lan - 10, num + 1)
    return draw_branch(t1, lan - 10, num + 1)
draw_branch(t, 100, 0)
