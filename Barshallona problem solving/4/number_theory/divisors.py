n = int(input())
# x = 1
# i = 1
# count = 0
# while x <= n:
#     i = x * x
#     if i >= n:
#         print(x)
#         exit()
#     x += 1
def check(num):
    if num * num <= n:
        return True
    else:
        return False
lo = 0
hi = n
res = 1
while lo <= hi:
    mid = (hi + lo ) // 2
    if check(mid):
        res = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(res)