n = int(input())
var = list(map(int, input().split()))
biggest = var[0]
position = 0
for i in range(n):
    if var[i] > biggest:
        biggest = var[i]
        position = i
biggest = 0
for i in range(n):
    if i != position and var[i] > biggest:
        biggest = var[i]
print(biggest)