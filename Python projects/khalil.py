import math
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sum(self):
        return (self.x * self.x) + (self.y * self.y)
    def distance(self):
        return math.sqrt(self.x * self.x + self.y * self.y)
z = 2
v = 7
def solve(x, y):
    if x * y > 7:
        print("soory", x , y)
        return 0
    if x + y == 2 and x * y == 7:
        print("x: ", "y: ")
        return 0
    x += 0.005
    y += 0.005
    return solve(x, y)
print(solve(3.5, 1.5))
