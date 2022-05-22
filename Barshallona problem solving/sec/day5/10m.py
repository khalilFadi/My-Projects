n, q = map(int, input().split())
a = list(map(int, input().split()))
x = int(input())
a.sort()
for _ in range(q):
    x = int(input())
    lo = 0
    hi = n - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] <= x:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    if res != -1 and a[res] == x:
        print("Yes")
    else:
        print("No")