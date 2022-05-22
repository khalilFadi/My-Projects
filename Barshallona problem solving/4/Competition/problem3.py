"""
function 
i have no idea
"""

a, b, c, d = map(int, input().split())
def f(x):
    return a * x**3 + b * x**2 + c *x + d
lo = -1000
hi = 1000
for i in range(200):
    mid = (lo + hi) /2
    if f(mid) * f(lo) > 0:
        lo = mid
    else:
        hi = mid
print(lo)
