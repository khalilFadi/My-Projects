num = int(input())

def findnum(n):
    m = 0
    for i in range(n):
        m += (10 ** i)
    return m
lo = 0
hi = num
mid = 0
last = num
for i in range(1, num + 1):
    if findnum(i) % num == 0:
        print(i)
        exit()
print(-1)