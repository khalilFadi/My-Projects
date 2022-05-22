m, k = map(int, input().split())
n = input()
res = ""
if k < 1:
    print(n)
    exit()
if len(n) == 1:
    print(0)
    exit()

if n[0] != '1':
    k -= 1
    res += '1'
else: 
    res += n[0]
i = 1
while k > 0 and i < len(n):
    if n[i] != '0':
        k -= 1
        res += '0'
    else:
        res += n[i]
    i += 1
res += n[i:len(n)]
print(res)
# 10 3
# 1001000111