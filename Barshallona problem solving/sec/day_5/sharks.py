n = int(input())
vers = []
for i in range(n):
    ver = list(map(float, input().split()))
    ver.append(ver[0] / ver[1])
    ver.append(ver[1] / ver[0])
    vers.append(ver)

bishops = 0
for i in range(n):
    for x in range(i + 1, n):
        if vers[i][2] == vers[x][2]:
            bishops += 1
for i in range(n):
    for x in range(i + 1, n):
        if vers[i][3] == vers[x][3]:
            bishops += 1
print(bishops)