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
var = list(map(int, input().split()))
var.sort()
lastDivisors = divisiors(var[0])
result = 0
for x in lastDivisors:
    works = True
    for i in var:
        if i % x:
            works = False
    result += works
        
print(result)