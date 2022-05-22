"""n, m = map(int, input().split())

dp = []
for i in range(n):
    var = list(map(int, input().split()))
    dp.append(var)
maxvalue = 0
def function(i, j, value):
    global maxvalue
    if i >= n or j >= m:
        return 0
    if i == n - 1 and j == m - 1:
        value += dp[i][j]
        if value > maxvalue:
            maxvalue = value
        return value
    value += dp[i][j]
    return function(i + 1, j, value), function(i,j + 1, value)

function(0,0,0)
print(maxvalue)"""
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
dp = [[0 for i in range(m)] for j in range(n)]

inf = -10**10
for i in range(n):
    for j in range(m):
        dp[i][j] = a[i][j]
        best = -inf
        if i > 0:
            best = max(best, dp[i - 1][j])
        if j > 0:
            best = max(best, dp[i][j - 1])
        if best != -inf:
            dp[i][j] += best
print(dp[n - 1][m - 1])