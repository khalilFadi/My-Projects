q = int(input())
for i in range(q):
    string = input()
    L, R, U, D = 0, 0, 0, 0
    for i in range(len(string)):
        o = string[i]
        if o == 'L':
            L += 1
        if o == 'R':
            R += 1
        if o == 'D':
            D += 1
        if o == 'U':
            U += 1
    leftRight = min(L, R)
    upDown = min(U, D)
    if leftRight == 0 and upDown == 0:
        print("0")
    elif leftRight == 0:
        print("2")
        print("UD")
    elif upDown == 0:
        print("2")
        print("LR")
    else:
        print(leftRight * 2 + upDown * 2)
        for i in range(upDown):
            print('U', end="")
        for i in range(leftRight):
            print("L", end="")
        for i in range(upDown):
            print("D", end="")
        for i in range(leftRight):
            print("R", end="")
        print("")