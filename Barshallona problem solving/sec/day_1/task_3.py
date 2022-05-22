num = int(input())
var = list(map(int, input().split()))
big = 0
pos = 0
for i in range(len(var)):
    if var[i] >= big:
        big = var[i]
        pos = i
var[pos], var[len(var) - 1] = var[len(var) - 1], var[pos]
for i in var:
    print(i, end=" ")