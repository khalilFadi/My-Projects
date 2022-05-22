num = int(input())
var = list(map(int, input().split()))
output = 0
def check_swap(i):
    global output
    if i + 1 == len(var):
        return 0
    if var[i] > var[i + 1]:
        var[i], var[i + 1] = var[i + 1], var[i]
        output += 1
    return check_swap(i + 1)
for i in range(len(var)):
    check_swap(0)
n = ((num * (num - 1)) / 2 ) - 1
trim = "YES" if output <= n else "NO"
print(trim)