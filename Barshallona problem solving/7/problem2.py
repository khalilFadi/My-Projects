n, m = map(int, input().split())
result = 0
dp = [i for i in range(n + 1)]
result = 0
for i in range(n):
    k = n - dp[i]
    for j in range(1, m):
        if k % j == 0:
            result += 1
print(result)