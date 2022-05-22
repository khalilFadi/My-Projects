def divisiors(n):
    ans = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            ans.append(n // i)
        i += 1
    return ans

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

n = int(input())
var = divisiors(n)
for i in range(0, len(var), 2):
    if is_prime(var[i]) and is_prime(var[i + 1]):
        print("YES")
        exit()

print("NO")