#longest increasing subsequence(LIS)
"""
    1 5 2 3 7 2 1
    1 -> 5 -> 7
    1 -> 2 -> 3 -> 7
"""
n = int(input())
a = list(map(int, input().split()))
dp = [1 for i in range(n)]
par = [-1 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[j] < a[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            par[i] = j
mx = max(dp)
ans = []
for i in range(n):
    if dp[i] == mx:
        m = i
        while True:
            ans.append(m + 1)
            m = par[m]
            if m == -1:
                break
        break
print(mx)
ans.reverse()
print(*ans)
 

