import math
def function(num):
    result = 0
    number = num 
    for i in range(1, num + 1):
        number -= 1
        result += int(num / i )
        if num / i <= 1:
            break
    result += number 
    return result
x = int(input())
output = 1
lo = 0
hi = 86764
res = 0
while lo <= hi:
    mid = (lo + hi) // 2
    if function(int(mid)) < x:
        res = mid
        lo = mid + 1
    else:
        hi = mid - 1
    
print(res + 1)