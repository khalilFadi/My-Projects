from turtle import *

t = Turtle()
s = Screen()
def run(x, y):
    t.goto(x, y)
def up():
    t.forward(100)
    
s.onclick(run)
s.onkey(up, "Up")
s.listen()
mainloop()