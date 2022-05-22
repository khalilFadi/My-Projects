""" the goal is to find 
the minumum distance bettwen the
red and blue light bulbs """
#find the one after and the one before using binary search
n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.sort()
y.sort()
def binary_search(v):
    lo = 0
    hi = m - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) / 2
        if y[mid] <= v:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res
for e in x:
    b = binary_search(e)
    if b == -1:
        closest = y[1]
    else:
        closest = y[b]
    if b != m - 1 and abs(y[b + 1] - e) < closest:
        closest = abs(y[b + 1] - e)
    mn = min(mn, closest)
print(mn)

