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
search = divisiors(var[0])
result = 0
for i in range(len(search)):
    yeah = True
    for x in var:
        if x % search[i] != 0: 
            False
    if yeah:
        result += 1
        print(search[i])
print(result)