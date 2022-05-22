num = int(input())
for i in range(num):
    a, b = map(int, input().split())
    if a == b:
        print(0)
        continue
    dif = abs(a - b)
    result = 0
    over = dif - (dif % 10)
    if dif % 10 != 0:
        result += 1
    result += over // 10
    print(result)