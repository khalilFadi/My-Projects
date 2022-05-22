m, n = map(int, input().split())
blue = list(map(int, input().split()))
red = list(map(int, input().split()))
lights = []

for i in range(m):
    lights.append((blue[i], 1))
for i in range(n):
    lights.append((red[i], 2))
lights.sort()

least_distance = 10e9
for i in range(len(lights) - 1):
    if lights[i][1] == 1 and lights[i + 1][1] == 2:
        if abs(lights[i][0] - lights[i][0]) < least_distance:
            least_distance = abs(lights[i + 1][0] - lights[i][0])
print(least_distance)