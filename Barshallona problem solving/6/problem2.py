num = int(input())
x, y = map(int, input().split())
result = num
startx, starty = x, y
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
for _ in range(num - 1):
    a, b = map(int, input().split())
    distanceA = abs(a - x)
    distanceB = abs(b - y)
    result += gcd(distanceA, distanceB) - 1
    x = a
    y = b
distanceA = abs(startx - x)
distanceB = abs(starty - y)
result += gcd(distanceA, distanceB) - 1
print(result)