
n, p = map(int, input().split())
num =  list(map(int, input().split()))

def number(ver, x):
    result = 0
    for i in ver:
        result += i // x
    return result
num.sort()
num.reverse()
hi = num[0]
output = 0
for i in range(num[0] + 1):
    if number(num, hi) >= p:
        output = hi
        break
    hi -= 1
print(output)