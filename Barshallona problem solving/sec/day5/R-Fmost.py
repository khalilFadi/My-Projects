n, q = map(int, input().split())
a = list(map(int, input().split()))
b = a[:]
for i, e in enumerate(a):
    a[i] =  (e, i + 1)
a.sort()
for _ in range(q):
    x = int(input())
    def right_most(arr, x):
        lo = 0
        hi = n - 1
        res = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid][0] <= x:
                res = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return res
    r = right_most(a, x)
    if r != -1 and a[r][0] == x:
        print(a[right_most(a, x - 1) + 1][1], a[r][1])
    else:
        print(-1, -1)
