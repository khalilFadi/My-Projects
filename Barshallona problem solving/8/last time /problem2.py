#Longest common subsequence (LCS)
""" 
cat + dog = 0
cat + bat = 2 "at"
"""
n, m = map(int, input().split())
s= input()
t = input()

dp = [[0 for i in range(m + 1)] for j in range(n+ 1)]

for i in range(n + 1):
    for j in range(m + 1):
        if i < n:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j < m:
            dp[i][j+ 1] = max(dp[i][j + 1], dp[i][j])
        if i < n and j < m:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (1 if s[i] == t[j] else 0))
print(dp[n][m])