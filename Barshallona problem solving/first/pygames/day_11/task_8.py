#circles thing 
import turtle
t = turtle.Turtle()
t.speed(0)
def draw_spiral(length, diffrence):
    while length > 0: 
        t.circle(length)
        length -= diffrence
for i in range(5):
    draw_spiral(100, 10)
    t.right(72)