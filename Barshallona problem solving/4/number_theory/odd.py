def divisiors(n):
    ans = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            if i * i != n:
                ans.append(n // i)
        i += 1
    return ans

n = int(input())
result = 0
for i in range(1, n + 1):
    if len(divisiors(i)) % 2 or len(divisiors(i)) == 1:
        result += 1
print(result)
