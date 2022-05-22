num = int(10**9 + 7)
p  = int(input())

if p % 2 == 1:
    print(0)
    exit()
else:
    k = 1
    for i in range(p // 2):
        k = k * (i + p // 2 + 1)
    for i in range(p // 2):
        k //=( i+1)
print(k % num)