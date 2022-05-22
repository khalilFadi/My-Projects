n, k = map(int, input().split())
vec = input()
res = ""
res += vec[0] if vec[0] == [1] else str(int(vec[0]) - 1)
if len(vec) == 1:
    print((len(vec) - 1 if vec[0] > 1 else 0))
    exit()

startingPoint = 1
for i in range(1, n):
    if k > 1:
        res += '0'
        k -= 1
        
    else:
        res += vec[i]
print(int(vec) - int(res))
