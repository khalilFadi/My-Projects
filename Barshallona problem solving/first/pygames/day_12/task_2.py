import turtle
import math
def turtle_movement(t, screen):
    def right():
        t.right(20)
    def left():
        t.left(20)
    screen.onkey(right, "Right")
    screen.onkey(left, "Left")
    screen.listen()
    return t