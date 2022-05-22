# #we want to et the first heater in the first position ??
# #the goal is to get the minimum distance 
#     #if we know the minimum distance then w can move directly to it 
#     """ k >= 3 else we can't do it"""
# #Time
#     """
#     we can do it with the min dist
#     o(n log n) sortig
#     O(n) O(log n)

#     """

n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

def is_opssible(dist):
    last_heater = x[0]
    number_of_heaters = 0
    for pos in x:
        if pos - last_heater >= dist:
            number_of_heaters += 1
            last_heater = pos
    return number_of_heaters >= k

lo = 1
hi = 10e9
res = 1

while lo <= hi:
    mid = (lo + hi) // 2
    if is_opssible(mid):
        res = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(res)