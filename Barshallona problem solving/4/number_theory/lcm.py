def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
var = list(map(int, input().split()))

for i in range(len(var) - 1):
    var[i + 1] = gcd(var[i], var[i + 1])
print(var[-1])