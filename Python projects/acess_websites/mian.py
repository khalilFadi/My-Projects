grid = []
for i in range(9):
    y1 = str(input())
    grid.append((y1))
print(grid)
#check y 
check = [[[i for i in range(10)] for i in range(9)] for i in range(9)]
current_num = 8

for y in range(8):
    fond = True if grid[y].find(str(current_num)) != -1 else False
    for x in range(8):
        if grid[y][x] == '-':
            if fond:
                check[y][x].remove(current_num)
        else:
            check[y][x] = [grid[y][x]]
print(grid)
