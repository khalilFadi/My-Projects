""" this will be about the christams
tree you need to get the number of branches
and workers from there you solve the problem"""
n, k = map(int, input().split())
t = list(map(int, input().split()))

def valid(m):
    current_partition = 0
    cnt = 1
    for i in t:
        if i > m:
            return False
        if current_partition + i > m:
            cnt += 1
            current_partition = i
        else:
            current_partition += i
        return cnt <= k

lo = 1
hi = 10e9 + 1
res = hi
while lo <= hi:
    mid = (lo + hi) / 2

    if valid(mid):
        res = mid
        hi = mid - 1
    else:
        lo = mid + 1
print(res)