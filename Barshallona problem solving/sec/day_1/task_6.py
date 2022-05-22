n, k = map(int,input().split())
var = list(map(int, input().split()))
result = 0
def search_largest():
    global result
    big = var[0]
    pos = 0
    for i in range(len(var)):
        if var[i] > big:
            big = var[i]
            pos = i
    result += big
    var[pos] = -1
    return 0
for i in range(k):
    search_largest()
print(result)
