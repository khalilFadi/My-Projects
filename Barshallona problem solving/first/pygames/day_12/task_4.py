import turtle

def turtle_movement(t, screen):
    def up():
        t.goto(int(t.xcor()), int(t.ycor()) + 30)
    def right():
        t.goto(int(t.xcor()) + 30, int(t.ycor()))
    def down():
        t.goto(int(t.xcor()), int(t.ycor()) + 30 * -1)
    def left():
        t.goto(int(t.xcor()) + 30 * -1, int(t.ycor()))

    screen.onkey(up, "Up")
    screen.onkey(up, "w")
    screen.onkey(down, "Down")
    screen.onkey(down, "s")
    screen.onkey(right, "Right")
    screen.onkey(right, "d")
    screen.onkey(left, "Left")
    screen.onkey(left, "a")
    return t