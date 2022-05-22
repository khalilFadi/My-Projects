# n m
# n1 n2 n3
# m1 m2
# result
# n1 <= m1 <= m2 <= n2 <= n3
num = list(map(int, input().split()))
m = num[1]
n = num[0]
ver_N = list(map(int, input().split()))
ver_M = list(map(int, input().split()))
result = []
#x with n
#y with m
x, y = 0, 0
result = []
while x < n and y < m:
    output = ver_N[x] if ver_N[x] < ver_M[y] else ver_M[y] 
    result.append(output)
    f = x
    x += 1 if ver_N[x] <= ver_M[y] else 0
    if x >= n: break
    y += 1 if not ver_N[x] < ver_M[y] and f == x else 0

while x < n:
    result.append(ver_N[x])
    x += 1
while y < m:
    result.append(ver_M[y])
    y += 1

print(*result)
