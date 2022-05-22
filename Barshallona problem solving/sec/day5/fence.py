n, k = map(int, input().split())
a = list(map(int, input().split()))

def possible(h):
    if h == 0:
        return True
    result = 0
    for e in a:
        result += e // h
    return result >= k

lo = 0
hi = 10e9
res = 0
while lo <= hi:
    mid = (lo + hi) // 2
    if possible(mid):
        res = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(int(res))