n = int(input())
dp = [(0, i) for i in range(n + 1)]
for i in range(2, n + 1):
    dp[i] = (dp[i - 1][0] + 1, i - 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], (dp[i // 2][0] + 1, i // 2))
    if i % 3 ==0:
        dp[i] = min(dp[i], (dp[i // 3][0] + 1, i // 3))
print(dp[n][0])
ans = [n]
while n != 1:
    n = dp[n][1]
    ans.append(n)

ans.reverse()
print(*ans)


