#Task 1
for i in range(2,100,2):
    print(i)

#Task 2
    y = 1
    x = 5
    for i in range(9):
        print(y + i," ", x + i)

#Task 3
    x = 5
    for i in range(5,-1,-1):
        print(i)

#Task 4
    for i in ["Goshep", "Gleen", "Sally"]:
        print("Happy Birthday: ", i)
    print("Best Wishes")

#Task 5:
    arry = [90, 80, 10]
    result = 0
    o = 0
    for i in arry:
        result += i
        o += 1
    print(result / o)

#Task 6:
    for i in range(0,6):
        if i % 3 != 0:
            print(i)

#Task 7:
    for i in range(0, 5001):
        if i % 5 == 0:
            print(i)
    
#Task 8:
    arr = [150, 2, 4, 5, 9]
    for i in arr:
        print(i * i)

#Task 9:
    for i in range(11):
        print(i * 12)

#Task 10:
    for i in range(5, 5000, 2):
        print(i, "odd")
        print(i+1, "even")

#Task 11:
    for i in range(-500, 5):
        if i >= 0:
            break
        print(i)

#task 12:
    for i in range(50, -5, -1):
        if i <= 0:
            break
        print(i)

#task 13:
    x = 1
    y = 1
    for i in range(10):
        print("*" * x)
        x += y
        if x > 5:
            y *= -1

#task 14:
    x = 1
    y = 0
    for i in range(9):
        print(x + y)
        c = x
        x = x + y
        y = c

#task 15:
    string = "khalil"
    x = 0
    y = 1
    for i in range(len(string) * 2 + 1):
        print("")
        x += y
        if x >= len(string):
            y *= -1
        for k in range(x):
            print(string[k], end = "")

#task 16:
    for i in range(10):
        for x in range(11):
            print(i * x, " ", end = "")
        print("")

#take 19:
    sum = 0
    for i in range(0, 9999):
        sum += i
    print(sum)

#take 17 + 18:
    import turtle 
    import random 

    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    colors = ["red", "blue", "green", "yellow"]
    def draw_square():
        for i in range(4):
            t.color(colors[i])
            t.forward(50)
            t.left(90)
    t.penup()
    t.goto(300,300)
    t.pendown()
    y = 1
    c = -1
    for i in range(14):
        t.sety(t.ycor() - 50)
        c *= -1
        for x in range(20):
            draw_square()
            t.setx(t.xcor() - (50 * c))

