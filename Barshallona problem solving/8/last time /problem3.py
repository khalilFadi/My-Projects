#longest  subplaindrome 
# astring that can read from both sides the same way 
n = int(input())
s = input()
dp = [[None for i in range(n)] for j in range(n)]

#memoize technique 
def solve(l, r):
    if dp[l][r]:
        return dp[l][r]
    if l > r:
        dp[l][r] = 0
        return dp[l][r]
    if l == r:
        dp[l][r] = 1
        return dp[l][r]
    dp[l][r] = 0
    dp[l][r] = max(dp[l][r], solve(l  +1, r))
    dp[l][r] = max(dp[l][r], solve(l, r - 1))
    dp[l][r] = max(dp[l][r], solve(l + 1, r - 1) + (2 if s[l] == s[r] else 0))
    return dp[l][r]

print(solve(0, n - 1))