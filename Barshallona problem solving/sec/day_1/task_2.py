n = int(input())
var = list(map(int, input().split()))
def find_samllest(start):
    small = var[start]
    pos = start
    for i in range(start,len(var)):
        if var[i] <= small:
            small = var[i]
            pos = i
    return pos
for i in range(len(var)):
    small = find_samllest(i)
    var[small], var[i] = var[i], var[small]
for i in var:
    print(i, end = " ")