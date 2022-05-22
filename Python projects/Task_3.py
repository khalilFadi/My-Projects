def Task0(): 
    var1 = input()
    var2 = input()
    var1 = list(var1)
    var2 = list(var2)
    out = True
    var1Mis = 0
    var2Mis = 0
    for i in range(len(var1)):
        result = False
        for x in range(len(var2)):
            if var1[i] == var2[x]:
                a = var2.pop(x)
                result = True
                break
        
        if result == False:
            out = False
            break 
    print(out)
def task1():
    inp = input()
    def p_b_sub(var):
        stri = ""
        for i in var:
            if i == 'p':
                stri += "b"
            else:
                stri += i
        return stri
    print(p_b_sub(inp))
def task2():
    def search(lis):
        for i in lis:
            if i == [0,0]:
                return True
        return False
    lis = [[1,1], [2,1], [0,0]]
    print(search(lis))
def task3():
    def search(lis):
        mx = 0
        pos = 0
        for i in lis:
            if  len(i) > mx:
                mx = len(i)
        return mx
    var = ["batata", "khalil",  "asdsadsadsad"]
    print(search(var))
def task4():
    def s_search(lis):
        result = []
        for i in lis:
            if i[0] == 's' or i[0] == 'S':
                result.append(i)
        return result
    var = ["apple", "snake", "Sasa"]
    print(s_search(var))
def task5():
    def sum(lis):
        result = 0
        for i in lis:
            result += i
        return result
    var = [0,1,2,3,1]
    print(sum(var))
def task6():
    def sum(lis1, lis2):
        result = []
        for i in range(len(lis1)):
            n = lis1[i] + lis2[i]
            result.append(n)
        return(result)
    var1 = [1,2,3, 4]
    var2 = [4, 3, 2, 1]
    print(sum(var1, var2))
def task7():
    def maximum(lis):
        mx = 0
        for i in lis:
            if i > mx:
                mx = i
        return mx
    print(maximum([0,1,2,3,4,5,6]))
def olympics():
    import turtle
    checkpoint = [0,0]
    def circle(t, direction = 1):
        for i in range(36):
            if i == checkpoint[0] or i == checkpoint[1]:
                t.penup()
            elif i == checkpoint[0] + 2 or i == checkpoint[1] + 2:
                t.pendown()
            t.forward(10)
            t.left(10 * direction)
    t = turtle.Turtle()
    t.speed(0)
    t.width(10)
    t.penup()
    t.forward(-150)
    t.pendown()
    #blue
    t.color("blue")
    circle(t)
    #green
    t.color("yellow")
    checkpoint[1] = 18
    checkpoint[0] = 27
    t.penup()
    t.goto(t.xcor()+ 10, t.ycor())
    t.pendown()
    t.right(90)
    t.pendown()
    circle(t)
    #black
    checkpoint[1] = 0
    checkpoint[0] = 9
    t.penup()
    t.goto(t.xcor()+ 60, t.ycor() + 63)
    t.pendown()
    t.color("black")
    circle(t)
    #green
    checkpoint[1] = 18
    checkpoint[0] = 27
    t.penup()
    t.goto(t.xcor()+ 60, t.ycor() - 63)
    t.pendown()
    t.color("green")
    circle(t)
    #red
    checkpoint[1] = 0
    checkpoint[0] = 0
    t.penup()
    t.goto(t.xcor()+ 60, t.ycor() + 63)
    t.pendown()
    t.color("red")
    circle(t)
def theWierdThing():
    import turtle
    t = turtle.Turtle()
    x = 0
    y = 1
    for i in range(100):
        t.forward((x)+i)
        t.right(15)
        x += 1
