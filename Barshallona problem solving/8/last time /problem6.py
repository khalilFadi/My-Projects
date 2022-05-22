n = int(input())
for x in range(n):
    var = input()
    dip = [[False for i in range(int(1e4))] for i in range(int(1e4))]
    x = 0
    y = 0
    L, R, U, D = 0, 0, 0, 0
    for i in var:
        if i == 'L':
            L += 1
        if i == 'R':
            R += 1
        if i == 'U':
            U += 1
        if i == 'D':
            D += 1
    if L > R:
        var.replace('L', '', abs(L - R))
    elif R > L:
        var.replace('R', '', abs(L - R))
    if U > D:
        var.replace('U', '', abs(U - D))
    elif D > U:
        var.replace('D', '', abs(U - D))    
    dip = [[False for i in range(int(U if U > D else D))] for i in range(int(L if L > R else R))]
    left = True
    for i in range(len(var)):
        pastx, pasty = x, y
        if var[i]== 'L':
            x -= 1
        if var[i]== 'R':
            x += 1
        if var[i]== 'U':
            y -= 1
        if var[i]== 'D':
            y += 1
        if dip[x][y] == True:
            x, y = pastx, pasty
            var[i], var[i + 1] = var[i + 1], var[i]
            i -= 1
            continue
        dip[x][y] = True
    print(var)