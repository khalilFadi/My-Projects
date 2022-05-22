x = int(input())
def function(num):
    return (42 * num * num * num) + (13 * num * num) + (1337 * num)
lo = 0
hi = x
res = 0
while lo <= hi:
    mid = (lo + hi) / 2
    m = function(mid)
    if m <= x:
        res = mid
        lo = mid + 1e-10
    else:
        hi = mid - 1e-10
if int(res) == res:
    res = (int(res))
print(res)