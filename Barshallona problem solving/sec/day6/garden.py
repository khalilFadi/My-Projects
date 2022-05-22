n, l = map(int,input().split())
var = list(map(int, input().split()))
max_num = 0

var.sort()
var.reverse()
def function():
    #lets test of finding the max distance bettwen all points 
    #ten we will add the first and last points distance and find out 
    global max_num
    for i in range(len(var) - 1):
        if var[i] - var[i + 1] > max_num:
            max_num = var[i] - var[i + 1]
lo = 0  
hi = l
res = 0
mid = l // 2
function()
nums = [var[-1],float(max_num / 2), l - var[-0]]
for i in nums:
    if i > res:
        res = i
print(res)
